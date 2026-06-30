"""Braider layer for emergent structural cache identity."""
from __future__ import annotations

import hashlib, json
from collections import defaultdict
from typing import Dict, List, Tuple

from .entries import BraiderOutput, PrimitiveStreams


def _digest(data) -> str:
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def braid_streams(streams: PrimitiveStreams) -> BraiderOutput:
    events: List[Dict[str, int]] = []
    triples: List[Tuple[int, int, int]] = []
    for i, triple in enumerate(zip(streams.angle_bits, streams.rotation_bits, streams.chirality_bits)):
        a, r, c = (int(x) & 1 for x in triple)
        triples.append((a, r, c))
        events.append({"index": i, "angle": a, "rotation": r, "chirality": c, "parity": (a ^ r ^ c)})
    windows = []
    seen = defaultdict(list)
    for i, triple in enumerate(triples):
        seen[triple].append(i)
    for triple, positions in seen.items():
        if len(positions) > 1:
            windows.append({"kind": "repeated_triple", "triple": triple, "positions": tuple(positions)})
    for width in range(2, min(5, len(triples)) + 1):
        subseqs = defaultdict(list)
        for i in range(0, len(triples) - width + 1):
            subseqs[tuple(triples[i:i + width])].append(i)
        for subseq, positions in subseqs.items():
            if len(positions) > 1:
                windows.append({"kind": "repeated_subsequence", "width": width, "positions": tuple(positions)})
    return BraiderOutput(streams, _digest(events), tuple(events), tuple(windows))
