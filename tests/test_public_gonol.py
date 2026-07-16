from __future__ import annotations

import pytest

from ucns import (
    ARITY,
    ORIGIN,
    PUBLIC_GONOL_157,
    PUBLIC_GONOL_SHA256,
    CarrierCharError,
    GonalSpec,
    PrivateGonal,
    char_of_vertex,
    chirality,
    decode_text_path,
    encode_text_path,
    face,
    get_default,
    is_seam_event,
    mirror_of,
    n_minus,
    n_plus,
    path_vertices,
    public_gonol_sha256,
    validate_gonal,
    vertex_of_char,
)


def test_exact_public_arrangement_and_digest():
    assert len(PUBLIC_GONOL_157) == 157
    assert len(set(PUBLIC_GONOL_157)) == 157
    assert PUBLIC_GONOL_157[0] == " "
    assert vertex_of_char("0") == 139
    assert public_gonol_sha256(PUBLIC_GONOL_157) == PUBLIC_GONOL_SHA256
    assert validate_gonal(get_default(), GonalSpec())["valid"] is True


def test_validator_rejects_malformed_carriers_and_moved_origin():
    spec = GonalSpec()

    short = validate_gonal([" "], spec)
    assert short["valid"] is False
    assert any("arity mismatch" in item for item in short["violations"])

    duplicated = validate_gonal([" "] * ARITY, spec)
    assert duplicated["valid"] is False
    assert any("origin must occur exactly once" in item for item in duplicated["violations"])
    assert any("duplicate glyphs" in item for item in duplicated["violations"])

    moved = list(PUBLIC_GONOL_157)
    moved[0], moved[1] = moved[1], moved[0]
    report = validate_gonal(moved, spec)
    assert report["valid"] is False
    assert any("fixed origin mismatch" in item for item in report["violations"])


def test_origin_faces_chirality_and_mirror_are_exact():
    assert ORIGIN == 0
    assert face(0) == 1
    assert face(78) == 1
    assert face(79) == -1
    assert face(156) == -1
    assert n_plus(156) == 0
    assert n_minus(0) == 156
    assert chirality(0, 1) == 1
    assert chirality(0, -1) == 156
    mirrored = mirror_of(get_default())
    assert mirrored[0] == " "
    assert mirror_of(mirrored) == get_default()


@pytest.mark.parametrize("text", ["aa", "aaa", "a a", "  ", "0", "10 01"])
def test_lifted_path_round_trip_and_monotonicity(text):
    path = encode_text_path(text)
    assert decode_text_path(path) == text
    assert all(path[i] < path[i + 1] for i in range(len(path) - 1))


def test_repeat_space_and_digit_zero_semantics():
    path = encode_text_path("aa")
    assert path[1] - path[0] == ARITY
    space_path = encode_text_path(" ")
    assert vertex_of_char(" ") == ORIGIN
    assert is_seam_event(space_path[0])
    assert decode_text_path(encode_text_path("  ")) == "  "
    assert vertex_of_char("0") != ORIGIN
    assert char_of_vertex(vertex_of_char("0")) == "0"
    assert path_vertices(encode_text_path("a a"))[1] == ORIGIN


def test_off_carrier_character_is_refused():
    with pytest.raises(CarrierCharError):
        vertex_of_char("☃")
    with pytest.raises(CarrierCharError):
        encode_text_path("hi ☃")


def test_private_transform_keeps_twist_origin_fixed_without_angle_projection():
    private = PrivateGonal.from_seed(b"public-gonol-test")
    assert private.perm[0] == ORIGIN
    assert set(private.perm[1:]) == set(range(1, ARITY))
    assert private.char_at(0) == " "
    assert not hasattr(private, "inscribe")
    advanced = private.advance(7, "deadbeef")
    assert advanced.perm[0] == ORIGIN
    assert advanced.perm == private.perm
    assert not hasattr(advanced, "inscribe")


def test_private_transform_rejects_noncanonical_or_invalid_frames():
    moved = list(PUBLIC_GONOL_157)
    moved[0], moved[1] = moved[1], moved[0]
    with pytest.raises(ValueError, match="custom PrivateGonal arrangements"):
        PrivateGonal.from_seed(b"bad-frame", moved)

    with pytest.raises(ValueError, match="must equal the canonical public gonol"):
        PrivateGonal(tuple(moved), 0, tuple(range(ARITY)))

    bad_perm = list(range(ARITY))
    bad_perm[0], bad_perm[1] = bad_perm[1], bad_perm[0]
    with pytest.raises(ValueError, match="must fix SPACE/ZERO"):
        PrivateGonal(PUBLIC_GONOL_157, 0, tuple(bad_perm))

    with pytest.raises(ValueError, match="phase must be in"):
        PrivateGonal(PUBLIC_GONOL_157, ARITY - 1, tuple(range(ARITY)))
