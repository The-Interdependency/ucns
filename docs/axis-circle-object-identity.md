# Axis-circle object identity candidate

UCNS already places a canonical residue r of an m-gonal visible boundary at
exactly r/m turns. This candidate applies that existing geometric relation to
one explicitly identified finite origin.

For an origin with N ordered axes and exact source receipt H:

    object(H, r, N) -> turn r/N

where r is the zero-based ordinal of one axis.

The resulting identity is the exact tuple:

    (origin receipt, axis count, axis ordinal, exact turn)

plus a deterministic SHA-256 over that canonical geometric record.

## Identity boundary

The geometric identity contains no label.

A downstream consumer may attach:

    heart
    cardiac
    corazón

or any other language/register surface to one axis identity without changing
that identity. Renaming is therefore a change in external attachment, not a
change in the UCNS object.

Changing the origin receipt, axis count, or axis ordinal changes the identity.

## Usage guidance

Construct one position only after the owning construction has closed a finite
ordered origin and produced an exact SHA-256 receipt for that origin:

    from ucns import build_axis_circle_position

    position = build_axis_circle_position(
        origin_sha256=origin_receipt,
        axis_count=axis_count,
        axis_ordinal=axis_ordinal,
    )

Consumers may store position.identity_sha256 as the stable geometric referent.
They must not move labels, dictionary definitions, translation claims, or
language semantics into UCNS.

## Standing

Candidate. The exact r/N mapping is inherited from the existing finite gonal
circle representation. This module does not establish that every future UCNS
object class must use a finite axis-origin circle.

## hmmm

Whether this finite-origin position identity becomes the universal UCNS object
identity across recursive/non-finite object classes remains unresolved.
