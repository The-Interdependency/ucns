import Lake
open Lake DSL

package «Ucns» where
  -- Minimal Lake package for the UCNS Theorem N formalization scaffold.
  -- See README.md: every statement here is currently `sorry`-backed and
  -- proves nothing. This package exists so the stubs type-check.

@[default_target]
lean_lib «Ucns» where
  -- Library root: Ucns/TheoremN.lean
