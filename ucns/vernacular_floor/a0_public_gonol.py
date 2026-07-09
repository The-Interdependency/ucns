# === RATIOS ===
# loc_comments: hmmm
# unresolved: upstream_a0_betatest_checkout_path, construction_hash
# === END RATIOS ===
"""Import boundary for the a0-betatest public gonol construction.

The vernacular floor does not rebuild the public carrier.  It imports
``interdependent_lib.gonal.gonal.EXAMPLE_157`` from an a0-betatest checkout or
from the active Python path and records the source module as provenance.
"""

from __future__ import annotations

import importlib
import sys
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Optional, Tuple, Union

PathLike = Union[str, Path]

A0_BETATEST_SOURCE_REPO = "a0-betatest"
A0_GONAL_MODULE = "interdependent_lib.gonal.gonal"
A0_PUBLIC_SYMBOL = "EXAMPLE_157"


@dataclass(frozen=True)
class A0PublicGonolConstruction:
    """Verbatim public gonol construction imported from a0-betatest."""

    source_repo: str
    construction_id: str
    glyphs: Tuple[str, ...]
    source_module: str = A0_GONAL_MODULE
    source_path: str = "hmmm"
    construction_hash: str = "hmmm"

    def confirm_a0_betatest(self) -> None:
        """Raise unless the construction was imported from the a0-betatest module."""

        if self.source_repo != A0_BETATEST_SOURCE_REPO:
            raise ValueError("public gonol construction must be imported from a0-betatest")
        if self.source_module != A0_GONAL_MODULE:
            raise ValueError("public gonol construction must come from interdependent_lib.gonal.gonal")
        if self.construction_id != A0_PUBLIC_SYMBOL:
            raise ValueError("public gonol construction must use EXAMPLE_157")


def import_a0_public_gonol(a0_betatest_path: Optional[PathLike] = None) -> A0PublicGonolConstruction:
    """Import ``EXAMPLE_157`` from a0-betatest and return its glyph sequence.

    If *a0_betatest_path* is supplied, it may point either at the repository root
    or its ``backend`` directory.  The path is prepended to ``sys.path`` only so
    Python can import a0-betatest's own package; the glyphs still come from that
    upstream module, not from a local UCNS reconstruction.
    """

    if a0_betatest_path is not None:
        backend_path = _backend_import_path(Path(a0_betatest_path))
        sys.path.insert(0, str(backend_path))
    module = importlib.import_module(A0_GONAL_MODULE)
    construction = construction_from_module(module)
    construction.confirm_a0_betatest()
    return construction


def construction_from_module(module: ModuleType) -> A0PublicGonolConstruction:
    """Build construction metadata from the imported a0-betatest gonal module."""

    glyphs = tuple(str(glyph) for glyph in getattr(module, A0_PUBLIC_SYMBOL))
    source_path = str(getattr(module, "__file__", "hmmm"))
    return A0PublicGonolConstruction(
        source_repo=A0_BETATEST_SOURCE_REPO,
        construction_id=A0_PUBLIC_SYMBOL,
        glyphs=glyphs,
        source_module=module.__name__,
        source_path=source_path,
    )


def _backend_import_path(path: Path) -> Path:
    """Return the importable a0-betatest backend path for repo-root or backend input."""

    if path.name == "backend":
        return path
    return path / "backend"


# === RATIOS ===
# loc_comments: hmmm
# unresolved: upstream_a0_betatest_checkout_path, construction_hash
# === END RATIOS ===
