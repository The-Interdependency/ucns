# UCNS candidate state for PTCNA

Status: implemented candidate producer; not UCNS or PTCNA canon.

## Usage

From an exact clean UCNS checkout, generate the receipt with its immutable
commit identity:

```bash
python -m ucns.ptcna_state \
  --repository-root "$PWD" \
  --producer-commit "$(git rev-parse HEAD)" \
  --output /tmp/ucns-ptcna-state.json
```

The receipt specifies the requested dense `157×7×7×53` PTCNA initialization
state as C-order little-endian float64 positive zeros. It carries the exact
157-position public-gonol provenance and hashes all 3,261,832 state bytes
without committing a multi-megabyte zero array.

Downstream PTCNA must consume the receipt through
`validate_ptcna_state_receipt`; reconstructing or shadowing this schema is not
an equivalent integration.

## Boundary

This candidate makes the integration question executable. It does not select
continuous seven-fold geometry, establish that the representation is useful,
transfer proof status, or establish production privacy. Those remain `hmmm`.
