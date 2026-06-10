import Lake
open Lake DSL

package «Ucns» where
  -- Lake package for the UCNS formalization.
  -- Statements not yet discharged are `sorry`-backed and prove nothing
  -- (see README.md: proof-status non-transfer discipline).

require std from git "https://github.com/leanprover/std4" @ "v4.7.0"

@[default_target]
lean_lib «Ucns» where
  -- Library root: Ucns.lean -> Ucns/Core.lean, Ucns/TheoremN.lean
