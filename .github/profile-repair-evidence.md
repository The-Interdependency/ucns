# EDCM/METAPAT profile repair evidence

This branch repairs the rejected placeholder implementation at commit `87a08edde5a6227f80425db5ee69c9558f6f440e`.

The repair:

- restores the complete current-root public surface;
- adds an immutable validated post-reset bridge record;
- requires explicit producer commit identity;
- binds structures to one fixed ordered-occurrence profile;
- preserves duplicate occurrence identity and order;
- keeps retained relation, state, and provenance layers outside scalar support;
- permanently forbids theorem, EDCM-measurement, and METAPAT-validity transfer;
- replaces placeholder tests with sixteen executable witnesses.

No archived factorization, universal multiplication, or `UCNSObject` authority is restored.
