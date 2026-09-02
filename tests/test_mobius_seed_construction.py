"""Regression tests for UCNS Mobius Seed construction state.

Usage guidance:
    Focused: ``python -m unittest tests.test_mobius_seed_construction``
    Discovery: ``python -m unittest discover -s tests``
"""

from __future__ import annotations

import unittest

from ucns.mobius_seed import BandSlot, MobiusSeedError, build_mobius_seed_of_life
from ucns.mobius_seed_construction import (
    ConstructionState,
    buildable_slots,
    construct,
    from_built,
    initial_construction_state,
)


class MobiusSeedConstructionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.seed = build_mobius_seed_of_life()
        self.initial = initial_construction_state(self.seed)

    def test_initial_state_builds_only_the_center(self) -> None:
        self.assertEqual(self.initial.built, frozenset((BandSlot.CENTER,)))
        # Every ring is a structural vesica of the center, so all six rings
        # are buildable next. This is the full one-step frontier of the
        # seven-band seed; later Flower-of-Life rings remain hmmm in UCNS.
        self.assertEqual(
            buildable_slots(self.initial),
            tuple(BandSlot)[1:],
        )

    def test_buildable_next_derives_from_structural_vesicas_only(self) -> None:
        state = construct(self.initial, BandSlot.RING_0)
        self.assertIn(BandSlot.RING_0, state.built)
        # All other rings remain buildable from the built center; the
        # incidental RING_0-RING_2 secant must not add a second-layer rule.
        self.assertEqual(
            buildable_slots(state),
            tuple(slot for slot in BandSlot if slot not in (BandSlot.CENTER, BandSlot.RING_0)),
        )

    def test_unbuildable_slot_fails_closed(self) -> None:
        state = construct(self.initial, BandSlot.RING_0)
        with self.assertRaises(MobiusSeedError):
            construct(state, BandSlot.RING_0)  # already built
        with self.assertRaises(MobiusSeedError):
            construct(state, BandSlot.CENTER)  # already built

    def test_full_construction_completes_all_seven_slots(self) -> None:
        state = self.initial
        while buildable_slots(state):
            state = construct(state, buildable_slots(state)[0])
        self.assertEqual(state.built, set(BandSlot))
        self.assertEqual(buildable_slots(state), ())

    def test_from_built_replays_a_persisted_slot_list(self) -> None:
        state = construct(construct(self.initial, BandSlot.RING_3), BandSlot.RING_2)
        replayed = from_built([BandSlot.CENTER, BandSlot.RING_3, BandSlot.RING_2], self.seed)
        self.assertEqual(replayed.built, state.built)

    def test_receipt_carries_no_game_semantics(self) -> None:
        payload = construct(self.initial, BandSlot.RING_1).as_dict()
        self.assertEqual(payload["schema_id"], "ucns.mobius-seed-construction")
        self.assertEqual(payload["selection_effect"], "none")
        for key in ("tile", "unit", "turn", "permission", "ahbg"):
            self.assertNotIn(key, str(payload).lower())


if __name__ == "__main__":
    unittest.main()
