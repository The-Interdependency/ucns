#!/usr/bin/env python3
"""Generate the bounded 3229-ladder fourth-power-coset audit.

The decimal ladder is

    k_m = int("3" + "2" * m + "9"),  n_m = 4*k_m + 1.

The frozen receipt covers exactly the terms whose ``n_m`` fits in an unsigned
64-bit integer. The factor schedule is deterministic, the primality test is
deterministic on that domain, and every recorded factorization is complete.
The result is incubating carrier-filter evidence, not UCNS canon and not a
cryptographic construction.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from math import gcd, prod
from pathlib import Path
from typing import Sequence


MAX_U64 = (1 << 64) - 1
FROZEN_MIN_M = 0
FROZEN_MAX_M = 17
JSON_RECEIPT = Path(__file__).with_name("3229_LADDER_ARITY_RECEIPT.json")
MARKDOWN_RECEIPT = Path(__file__).with_name("3229_LADDER_ARITY_RECEIPT.md")

# These bases make Miller-Rabin deterministic for every unsigned 64-bit input.
MILLER_RABIN_BASES_U64 = (2, 325, 9_375, 28_178, 450_775, 9_780_504, 1_795_265_022)
SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def ladder_k(m: int) -> int:
    """Return 3, followed by m copies of 2, followed by 9."""

    if isinstance(m, bool) or not isinstance(m, int) or m < 0:
        raise ValueError("m must be a non-negative integer")
    return int("3" + "2" * m + "9")


def ladder_n(m: int) -> int:
    return 4 * ladder_k(m) + 1


def is_prime_u64(value: int) -> bool:
    """Deterministic Miller-Rabin primality test on unsigned 64-bit inputs."""

    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("primality input must be an integer")
    if value < 2:
        return False
    if value > MAX_U64:
        raise ValueError("deterministic primality boundary is unsigned 64-bit")
    for prime in SMALL_PRIMES:
        if value % prime == 0:
            return value == prime

    odd_part = value - 1
    power_of_two = 0
    while odd_part % 2 == 0:
        power_of_two += 1
        odd_part //= 2

    for base in MILLER_RABIN_BASES_U64:
        if base % value == 0:
            continue
        witness = pow(base, odd_part, value)
        if witness in (1, value - 1):
            continue
        for _ in range(power_of_two - 1):
            witness = witness * witness % value
            if witness == value - 1:
                break
        else:
            return False
    return True


def pollard_brent_factor(value: int) -> int:
    """Return a non-trivial factor using deterministic Brent-Pollard schedules."""

    if value % 2 == 0:
        return 2
    if value % 3 == 0:
        return 3

    # Increasing c supplies a deterministic retry when one cycle degenerates.
    for constant in range(1, 256):
        state = 2
        block_size = 128
        divisor = 1
        radius = 1
        product_of_differences = 1
        saved_state = state

        while divisor == 1:
            anchor = state
            for _ in range(radius):
                state = (state * state + constant) % value
            offset = 0
            while offset < radius and divisor == 1:
                saved_state = state
                for _ in range(min(block_size, radius - offset)):
                    state = (state * state + constant) % value
                    product_of_differences = (
                        product_of_differences * abs(anchor - state) % value
                    )
                divisor = gcd(product_of_differences, value)
                offset += block_size
            radius *= 2

        if divisor == value:
            while True:
                saved_state = (saved_state * saved_state + constant) % value
                divisor = gcd(abs(anchor - saved_state), value)
                if divisor > 1:
                    break
        if divisor != value:
            return divisor
    raise RuntimeError(f"deterministic factor schedule exhausted for {value}")


def factor_u64(value: int) -> tuple[int, ...]:
    """Return the complete prime factorization with multiplicity."""

    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("factorization input must be a positive integer")
    if value > MAX_U64:
        raise ValueError("deterministic factorization boundary is unsigned 64-bit")
    factors: list[int] = []

    def split(part: int) -> None:
        if part == 1:
            return
        if is_prime_u64(part):
            factors.append(part)
            return
        divisor = pollard_brent_factor(part)
        split(divisor)
        split(part // divisor)

    split(value)
    factors.sort()
    result = tuple(factors)
    if prod(result) != value or not all(is_prime_u64(factor) for factor in result):
        raise AssertionError("factorization did not replay to certified prime factors")
    return result


def factor_powers(factors: Sequence[int]) -> tuple[tuple[int, int], ...]:
    return tuple(sorted(Counter(factors).items()))


def euler_phi_from_factorization(powers: Sequence[tuple[int, int]]) -> int:
    return prod((prime - 1) * prime ** (exponent - 1) for prime, exponent in powers)


def fourth_power_coset_arity(powers: Sequence[tuple[int, int]]) -> int:
    """Return [U(n):U(n)^4] from an odd prime-power factorization of n.

    For odd p, U(p**e) is cyclic of order phi(p**e). The kernel of x -> x**4
    has gcd(4, phi(p**e)) elements. The Chinese remainder theorem multiplies
    these kernel sizes, and the homomorphism theorem identifies that product
    with the index of the fourth-power image.
    """

    if any(prime == 2 for prime, _ in powers):
        raise ValueError("this audit formula is restricted to odd ladder values")
    return prod(
        gcd(4, (prime - 1) * prime ** (exponent - 1))
        for prime, exponent in powers
    )


def enumerated_fourth_power_coset_arity(modulus: int) -> int:
    """Direct finite control used only for small ladder moduli."""

    units = tuple(value for value in range(1, modulus) if gcd(value, modulus) == 1)
    image = {pow(value, 4, modulus) for value in units}
    if len(units) % len(image):
        raise AssertionError("fourth-power image order must divide the unit-group order")
    return len(units) // len(image)


def factorization_expression(powers: Sequence[tuple[int, int]]) -> str:
    return " * ".join(
        str(prime) if exponent == 1 else f"{prime}^{exponent}"
        for prime, exponent in powers
    )


def ladder_row(m: int) -> dict[str, object]:
    k = ladder_k(m)
    modulus = 4 * k + 1
    if modulus > MAX_U64:
        raise ValueError("ladder row exceeds the frozen deterministic factor boundary")
    factors = factor_u64(modulus)
    powers = factor_powers(factors)
    unit_group_order = euler_phi_from_factorization(powers)
    arity = fourth_power_coset_arity(powers)
    image_order, remainder = divmod(unit_group_order, arity)
    if remainder:
        raise AssertionError("fourth-power coset arity must divide the unit-group order")
    if modulus <= 2_000_000:
        assert enumerated_fourth_power_coset_arity(modulus) == arity
    return {
        "m": m,
        "k_decimal": str(k),
        "n": modulus,
        "n_equals_4k_plus_1": modulus == 4 * k + 1,
        "factorization": [
            {
                "prime": prime,
                "exponent": exponent,
                "prime_power": prime**exponent,
                "unit_group_order": (prime - 1) * prime ** (exponent - 1),
                "fourth_power_coset_factor": gcd(
                    4, (prime - 1) * prime ** (exponent - 1)
                ),
            }
            for prime, exponent in powers
        ],
        "factorization_expression": factorization_expression(powers),
        "factorization_status": "COMPLETE",
        "is_prime": len(powers) == 1 and powers[0][1] == 1,
        "omega_with_multiplicity": len(factors),
        "distinct_prime_factors": len(powers),
        "unit_group_order": unit_group_order,
        "fourth_power_image_order": image_order,
        "fourth_power_coset_arity": arity,
        "label": "HIT" if arity == 4 else "CONTROL",
    }


def build_receipt(
    min_m: int = FROZEN_MIN_M, max_m: int = FROZEN_MAX_M
) -> dict[str, object]:
    if min_m < 0 or max_m < min_m:
        raise ValueError("receipt range must satisfy 0 <= min_m <= max_m")
    if ladder_n(max_m) > MAX_U64:
        raise ValueError("receipt range exceeds the unsigned 64-bit factor boundary")

    rows = [ladder_row(m) for m in range(min_m, max_m + 1)]
    hits = [row["m"] for row in rows if row["label"] == "HIT"]
    controls = [row["m"] for row in rows if row["label"] == "CONTROL"]
    prime_hits = [row["m"] for row in rows if row["label"] == "HIT" and row["is_prime"]]
    composite_hits = [
        row["m"] for row in rows if row["label"] == "HIT" and not row["is_prime"]
    ]
    first_excluded_m = max_m + 1
    first_excluded_n = ladder_n(first_excluded_m)

    receipt = {
        "schema": "ucns-prime-arity-3229-ladder-audit-v1",
        "standing": "INCUBATING_UNRESOLVED_CARRIER_FILTER_EVIDENCE",
        "canon_status": "NONE",
        "verdict": "UNRESOLVED",
        "ladder": {
            "definition": 'k_m = int("3" + "2" * m + "9")',
            "modulus": "n_m = 4*k_m + 1",
            "min_m": min_m,
            "max_m": max_m,
            "term_count": len(rows),
        },
        "factorization_boundary": {
            "primality_domain": "positive unsigned 64-bit integers",
            "factorization_scope": "the emitted ladder rows",
            "maximum": MAX_U64,
            "method": "deterministic Miller-Rabin plus deterministic Brent-Pollard splitting",
            "all_emitted_rows_complete": True,
            "next_m": first_excluded_m,
            "next_k_decimal": str(ladder_k(first_excluded_m)),
            "next_n": first_excluded_n,
            "next_n_exceeds_boundary": first_excluded_n > MAX_U64,
        },
        "arity_definition": {
            "unit_group": "U(n) = (Z/nZ)^x",
            "fourth_power_image": "U(n)^4 = {x^4 mod n : x in U(n)}",
            "arity_4": "[U(n):U(n)^4]",
            "odd_prime_power_rule": "product over p^e || n of gcd(4, phi(p^e))",
            "label_rule": "HIT iff arity_4 == 4; CONTROL otherwise",
        },
        "rows": rows,
        "summary": {
            "hits": len(hits),
            "controls": len(controls),
            "hit_m": hits,
            "control_m": controls,
            "prime_hit_m": prime_hits,
            "composite_hit_m": composite_hits,
            "hit_is_not_a_primality_test": bool(prime_hits and composite_hits),
        },
        "validation": {
            "direct_unit_enumeration_m": [
                row["m"] for row in rows if row["n"] <= 2_000_000
            ],
            "direct_unit_enumeration_limit": 2_000_000,
            "stored_receipt_check": (
                "python3 docs/prime-arity/audit_3229_ladder_arity.py "
                "--check-receipts"
            ),
        },
        "claims": [
            "Each emitted factorization is complete within the declared boundary.",
            "Each emitted fourth-power coset arity follows from the recorded factorization.",
            "HIT is only the predicate arity_4 == 4.",
        ],
        "nonclaims": [
            "The decimal ladder is not UCNS canon.",
            "HIT does not identify primes, successor primes, cryptographic secrets, or keys.",
            "This audit does not construct the unresolved coset-to-prime map P(C).",
            "Carrier-filter evidence does not establish cryptographic advantage.",
        ],
        "hmmm": (
            "The ladder supplies a reproducible carrier filter, but no UCNS law currently "
            "selects the ladder or turns an arity-four HIT into a prime-speaking rule."
        ),
    }

    if min_m == FROZEN_MIN_M and max_m == FROZEN_MAX_M:
        assert ladder_n(FROZEN_MAX_M) <= MAX_U64
        assert ladder_n(FROZEN_MAX_M + 1) > MAX_U64
        assert hits == [0, 1, 2, 5, 7, 8]
        assert controls == [3, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        assert prime_hits == [0, 2, 5]
        assert composite_hits == [1, 7, 8]
    return receipt


def json_receipt_bytes(receipt: dict[str, object]) -> bytes:
    return (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode("utf-8")


def markdown_receipt_bytes(receipt: dict[str, object]) -> bytes:
    rows = receipt["rows"]
    assert isinstance(rows, list)
    summary = receipt["summary"]
    assert isinstance(summary, dict)
    boundary = receipt["factorization_boundary"]
    assert isinstance(boundary, dict)
    ladder = receipt["ladder"]
    assert isinstance(ladder, dict)
    json_digest = sha256(json_receipt_bytes(receipt)).hexdigest()
    if boundary["next_n_exceeds_boundary"]:
        boundary_text = (
            f"All emitted rows are completely factored inside the unsigned 64-bit "
            f"boundary. The next row, m={boundary['next_m']}, has "
            f"n={boundary['next_n']} and is deliberately excluded because it exceeds "
            "that frozen deterministic domain."
        )
    else:
        boundary_text = (
            f"All emitted rows are completely factored. This requested range stops at "
            f"m={ladder['max_m']}; its next row remains inside the unsigned 64-bit "
            "primality domain."
        )

    lines = [
        "# 3229-Ladder Fourth-Power-Coset Audit Receipt",
        "",
        "Status: `INCUBATING` / `UNRESOLVED`",
        "",
        "This is deterministic carrier-filter evidence. It is not UCNS canon, a",
        "coset-to-prime constructor, or a cryptographic primitive.",
        "",
        "## Frozen construction",
        "",
        "```text",
        'k_m = int("3" + "2" * m + "9")',
        "n_m = 4*k_m + 1",
        f"m = {ladder['min_m']}..{ladder['max_m']}",
        "label = HIT iff [U(n):U(n)^4] == 4; CONTROL otherwise",
        "```",
        "",
        f"JSON receipt SHA-256: `{json_digest}`",
        "",
        "## Results",
        "",
        "| m | k | n | complete factorization | phi(n) | image order | arity_4 | label |",
        "|---:|---:|---:|:---|---:|---:|---:|:---|",
    ]
    for row in rows:
        assert isinstance(row, dict)
        lines.append(
            "| {m} | {k_decimal} | {n} | `{factorization_expression}` | "
            "{unit_group_order} | {fourth_power_image_order} | "
            "{fourth_power_coset_arity} | **{label}** |".format(**row)
        )
    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- HIT rows: {summary['hit_m']}",
            f"- CONTROL rows: {summary['control_m']}",
            f"- Prime HIT rows: {summary['prime_hit_m']}",
            f"- Composite HIT rows: {summary['composite_hit_m']}",
            "- Therefore HIT is not a primality test.",
            "",
            "## Feasibility boundary",
            "",
            boundary_text,
            "",
            "## Standing",
            "",
            "```text",
            "3229-ladder generation: REPLAYED",
            "emitted factorizations: COMPLETE",
            "fourth-power coset arities: DERIVED",
            "carrier-filter significance: UNRESOLVED",
            "canon status: NONE",
            "cryptographic significance: UNRESOLVED",
            "```",
            "",
            "## hmmm",
            "",
            str(receipt["hmmm"]),
            "",
        ]
    )
    return "\n".join(lines).encode("utf-8")


def write_receipts(receipt: dict[str, object]) -> None:
    JSON_RECEIPT.write_bytes(json_receipt_bytes(receipt))
    MARKDOWN_RECEIPT.write_bytes(markdown_receipt_bytes(receipt))


def check_receipts(receipt: dict[str, object]) -> None:
    expected = {
        JSON_RECEIPT: json_receipt_bytes(receipt),
        MARKDOWN_RECEIPT: markdown_receipt_bytes(receipt),
    }
    for path, content in expected.items():
        if not path.is_file():
            raise SystemExit(f"missing receipt: {path}")
        if path.read_bytes() != content:
            raise SystemExit(f"receipt drift: {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write-receipts", action="store_true")
    action.add_argument("--check-receipts", action="store_true")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--min-m", type=int, default=FROZEN_MIN_M)
    parser.add_argument("--max-m", type=int, default=FROZEN_MAX_M)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if (args.write_receipts or args.check_receipts) and (
        args.min_m != FROZEN_MIN_M or args.max_m != FROZEN_MAX_M
    ):
        raise SystemExit("stored receipts use only the frozen m=0..17 range")
    receipt = build_receipt(args.min_m, args.max_m)
    if args.write_receipts:
        write_receipts(receipt)
    elif args.check_receipts:
        check_receipts(receipt)
    elif args.format == "markdown":
        print(markdown_receipt_bytes(receipt).decode("utf-8"), end="")
    else:
        print(json_receipt_bytes(receipt).decode("utf-8"), end="")


if __name__ == "__main__":
    main()
