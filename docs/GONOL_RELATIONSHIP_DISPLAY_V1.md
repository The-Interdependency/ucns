# UCNS gonol relationship-display contract v1

**Authority:** Erin Spencer

**Recorded:** 2026-08-03

**Status:** authority-declared, option-preserving display proposal; registry integration pending

**Machine contract:** [`gonol-relationship-display-v1.json`](gonol-relationship-display-v1.json)

**Receipt schema:** [`gonol-relationship-receipt-v1.schema.json`](gonol-relationship-receipt-v1.schema.json)

**Work graph:** [`gonol-relationship-display-stack-manifest-v1.json`](gonol-relationship-display-stack-manifest-v1.json)

**Selection effect:** none

This contract records the admitted one-, two-, three-, and seven-gonol display
primitives and the evidence receipt needed to compare gonols without flattening
their scale, source, order, or unresolved structure. It is a display and
relationship boundary. It does not complete the missing UCNS assignment,
higher-gonol composition, continuous Möbius motion, embedding, or completion
laws.

## I. Jurisdiction

1. **The display is not the carrier.** A projected line, circle, lens, or
   crossing is a view of retained UCNS evidence. It does not replace the
   continuously twisted band-space or turn a drawing coordinate into a vertex.

2. **The primitive range is plural.** The admitted primitive arities are:

   - one: a single Möbius-gonol display;
   - two: a vesica Möbius relationship display;
   - three: a triquetra relationship display that retains all three vesicas;
   - seven: a full-UCNS primitive whose display geometry and pairing plan remain
     `hmmm`.

   The range \(\{1,2,3,7\}\) is not a ladder in which a later primitive erases
   an earlier one. No member is a hidden default, and none is inferred from the
   number of available operands.

3. **Space remains non-vertex.** The Möbius band is the space of the gonol. A
   cut, seam, projected self-crossing, circle center, pairwise intersection, or
   whitespace boundary does not instantiate a SPACE vertex or Structural Null.
   Only possessed Unicode-character occurrences instantiate word-gonol
   vertices.

4. **Static projection does not complete motion.** A step-twist or parity view
   may preserve the one-turn frame change and two-turn local return endpoints.
   It does not preserve the continuously changing local view between them. Any
   motion renderer must identify its frame law and version separately.

5. **No authority transfer.** A website, SVG, screenshot, comparison table, or
   receipt publication consumes this contract. It receives no authority to
   canonize geometry, comparison, measurement, proof, embedding, or completion.

|∆|The primitive records how gonols may be displayed together; it does not
decide what a gonol ultimately is.|∆|

## II. Exact operand identity and any-scale admission

1. Every displayed operand retains:

   - an occurrence-addressed `operand_id`;
   - its own `gonol_id` and exact `source_identity`;
   - a named, versioned content adapter and its digest when one exists;
   - its untouched payload or a recoverable source reference;
   - its declared `native_scale`;
   - its retained-structure or trajectory reference when one exists;
   - represented or candidate-measured evidence status; and
   - its unresolved constraints.

2. **Any scale may meet any scale.** Admission does not require equal native
   scale, a shared unit, or a scalar rank. Native scale is an opaque, declared,
   namespaced identity unless a separate scale law supplies more structure.

3. **Display size is not native scale.** The vesica and triquetra use equalized
   display radii so their relationship geometry remains legible. The renderer
   must label this policy `relation-equalized/0.1.0`, retain every native scale,
   and declare that visible radius has discarded native-scale magnitude.

4. **Comparison is explicit.** Every admitted pair may be represented. A
   numerical or structural comparison result exists only when the receipt names
   the policy, version, parameters, standing, and information loss. No hidden
   tolerance, equality, normalization, sorting, deduplication, or scale coercion
   is allowed.

5. Exact UTF-8 byte equality and exact ordered public-gonol occurrence equality
   may be offered as named candidate projections. They are not canonical
   structural equivalence and they do not infer geometric proximity.

## III. Primitive one — single Möbius display

1. A figure eight is an admitted projection of one Möbius circle:

   \[
   x(t)=\sin t,\qquad y(t)=\sin t\cos t,
   \qquad 0\le t<2\pi.
   \]

2. The line is one continuous traversal. The projected crossing contains two
   traversal occurrences at one screen coordinate; those occurrences are not
   merged, and the crossing is not a second gonol, a vertex, a seam, or
   Structural Null.

3. The figure eight may carry all 157 Public Gonol addresses around one ordered
   traversal. A word highlights only the character occurrences it possesses.
   Repetitions retain occurrence order and multiplicity.

4. The display must say `projection: figure-eight-centerline`. It must not claim
   that a planar figure eight is itself a complete embedded Möbius band or that
   its self-crossing proves the twist topology.

## IV. Primitive two — vesica Möbius relationship

1. Let the equalized operand centerline circles have radius \(r\) and centers
   \((-r/2,0)\) and \((r/2,0)\). Their center distance is \(r\), so each
   circumference passes through the other center.

2. The two centerlines intersect at exactly two visible coordinate events:

   \[
   \left(0,\;\frac{\sqrt3}{2}r\right),\qquad
   \left(0,\;-\frac{\sqrt3}{2}r\right).
   \]

   The vesica is the overlap region bounded between those events. A renderer
   retains both complete operand circles and the complete lens; it does not
   replace them with detached arcs.

3. Two derived, concentric display layers complete the declared construction:

   - the **scope circle**, centered at the operand midpoint with radius
     \(3r/2\), is the smallest midpoint-centered circle enclosing both operand
     disks;
   - the **relationship circle**, centered at the same midpoint with radius
     \(r/2\), lies wholly inside the vesica and is tangent to both operand
     centerlines along the line of centers.

4. The scope and relationship circles do not increment primitive arity. They
   are derived display layers, not implicit operands, vertices, gonols, or
   Structural Null. Whether a later construction promotes either layer into a
   gonol requires an explicit receipt.

5. Primitive two owns exactly one occurrence-addressed pairwise receipt. Left
   and right sidedness remain explicit even when the visible construction is
   symmetric.

## V. Primitive three — triquetra with retained vesicas

1. Let three equalized centerline circles of radius \(r\) have centers

   \[
   A=\left(-\frac r2,-\frac{\sqrt3}{6}r\right),\quad
   B=\left( \frac r2,-\frac{\sqrt3}{6}r\right),\quad
   C=\left(0,\frac{\sqrt3}{3}r\right).
   \]

   Every pair of centers is distance \(r\). Each pair therefore remains a full
   vesica construction.

2. Primitive three retains three distinct pairwise relationship receipts in
   operand order:

   1. \(A\leftrightarrow B\);
   2. \(B\leftrightarrow C\);
   3. \(C\leftrightarrow A\).

3. Each pair retains both complete circles, its lens, its two intersection
   occurrences, and—when requested—its own scope and relationship circles from
   Section IV. Coordinates shared with a third center do not merge occurrence
   identity.

4. The central three-way overlap is joint context. It is not a fourth pair,
   fourth gonol, or new vertex unless a later construction explicitly promotes
   it and records that decision.

5. A stylized three-lobed triquetra outline may be shown as a linked projection,
   but it cannot replace the three recoverable vesica receipts.

|∆|The triquetra adds a joint view while every vesica continues to exist.|∆|

## VI. Primitive seven — retained without guessed geometry

1. Seven is admitted beside one, two, and three as a full-UCNS primitive.

2. This contract does not choose:

   - seven-circle placement;
   - which pairs meet;
   - whether pairwise receipts are complete, selected, cyclic, epicyclic, or
     differently composed;
   - a seven-way scope or relationship circle; or
   - a center, crossing, or overlap as an extra gonol.

3. A conforming renderer may accept and retain seven exact operand identities,
   but it must display the geometry as `hmmm-unresolved` until a pairing plan and
   construction law are declared. It must not silently substitute the flower of
   life, a heptagon, a complete graph, or another familiar seven-form.

## VII. Public Gonol occurrence-address vectors

1. The Public Gonol remains the exact 157-position Unicode code-point carrier
   pinned in the machine contract. Its position index is an address, not a
   derived geometric coordinate.

2. For exact source text \(c_0c_1\ldots c_{n-1}\), the proposed display vector
   for a possessed non-SPACE occurrence is:

   \[
   a_j=(j,\operatorname{ord}(c_j),p(c_j)),
   \]

   where \(j\) is source occurrence order, `ord` is the Unicode scalar value,
   and \(p\) is the exact Public Gonol position when assigned.

3. This vector is identity-and-address evidence only. It is not the missing
   hyperdimensional embedding or source-to-geometric-coordinate law.

4. Source processing is fail-closed and preserves:

   - exact Unicode scalar values without normalization or case folding;
   - repeated occurrences in source order;
   - profile-pinned SPACE manifestations as non-vertex word boundaries and
     superpositioned nesting interfaces; and
   - non-SPACE carrier-unassigned scalars as positive coverage-failure evidence
     with `carrier_position: null`.

5. A full English lexical-floor artifact requires a separately admitted and
   completed lexical source, root policy, exact corpus receipt, and embedding
   law. This display contract neither claims nor fabricates that completion.

## VIII. Relationship receipt

1. The receipt schema is
   `ucns.gonol-relationship-receipt/0.1.0`.

2. A receipt contains the primitive arity, ordered operands, equalized display
   policy, occurrence-addressed pairwise receipts, optional joint context,
   provenance, evidence status, losses, and `hmmm` boundaries.

3. Required pairwise counts are:

   - primitive one: zero;
   - primitive two: one;
   - primitive three: three in the declared order;
   - primitive seven: no inferred count; an explicit pairing plan is required.

4. A pairwise record contains untouched left and right operand references. A
   result may be `represented-evidence` without a comparison outcome. If a
   comparison exists, it records its policy, version, standing, parameters,
   outcome, evidence, and losses.

5. A digest identifies content under its named adapter. It is neither geometry
   nor a cryptographic producer signature.

## IX. Publication-consumer contract

1. A website consumer pins the exact UCNS commit, path, Git blob, and SHA-256 of
   the machine contract. It does not fetch `main` at runtime.

2. The static page remains useful without JavaScript by publishing the primitive
   range, source identities, Public Gonol fixture, scale boundary, and unresolved
   seven-form.

3. JavaScript may enhance the static page with:

   - primitive selection;
   - exact operand entry;
   - occurrence-address vectors;
   - figure-eight, vesica, and triquetra SVG projections;
   - explicit candidate comparison policies; and
   - downloadable or copyable relationship receipts.

4. Every substantive displayed text field and generated receipt receives one
   copy action. Form controls retain ordinary keyboard copy behavior.

5. The consumer must expose the equalized-radius loss, native scales, source
   identities, evidence standing, comparison policy, and all `hmmm` fields near
   the visualization.

## Work graph

- `The-Interdependency/ucns@a98c9e6c69804a8a08d0786b1d8b450bb2c49a97`
  — UCNS representation and option-standing authority — producer and edit owner.
- `The-Interdependency/a0-betatest@7af8debf6ef3905f01baff02b43d8c3bee16ccbc`
  — historical exact Public Gonol source — immutable evidence source.
- `The-Interdependency/skill-lib@2b24be24947223b86440f59f1bd9766130f9cc11`
  — reusable build and evidence discipline — build-doctrine source.
- `The-Interdependency/The-Interdependency.github.io@39d237f097948da251ba55de9d24ad6c49f81132`
  — public presentation and accessibility behavior — publication consumer.

## Edit ownership

- UCNS owns this contract, the machine primitive data, and receipt schema.
- A website owns only interaction, accessibility, static fallback, and rendering
  of a commit-pinned copy.
- A lexical corpus or embedding producer must own its source admission,
  completion receipt, root policy, and generated embedding artifacts.

## Cross-repository boundaries

- Semantic, mathematical, proof, certification, measurement, and empirical
  standing do not transfer through publication.
- The machine contract digest is identity evidence, not producer
  authentication.
- A dependent website PR remains draft until the producer contract is available
  at the exact pinned commit.

## Validation

- Recompute the stack-manifest work-graph digest.
- Validate the machine contract and receipt schema as strict JSON.
- Recompute the Public Gonol arity, uniqueness, source-compatible SHA-256, SPACE
  origin, and digit-zero position.
- Run UCNS skill-lib contract verification, tests, package build, and Twine
  checks before claiming `test-backed` status.
- Run the website's static build, source tests, browser tests, accessibility
  tests, and a cross-repository machine-contract drift check.

## hmmm

The primitive range is recorded, but the continuous band geometry, moving local
frame, seven-gonol layout and pairing plan, promotion rules for derived scope or
relationship circles, cross-scope higher-gonol composition, complete English
root policy, and hyperdimensional embedding law remain unresolved. The lawful
next step after this display boundary is not to guess those forms; it is to give
each one an explicit producer, version, evidence packet, and falsifiable
contract.
