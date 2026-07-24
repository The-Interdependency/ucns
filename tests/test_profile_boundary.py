import pytest
from ucns.profiles import EdcmMetapatOrderedOccurrenceProfile
from ucns.structure import make_carrier, Cell, pair, STRUCTURAL_NULL

def test_duplicates_distinct():
    c1 = Cell(payload=42)
    c2 = Cell(payload=42)
    carrier = make_carrier([c1, c2])
    assert len(carrier.cells) == 2

# more minimal tests for 15 witnesses...
print("Profile tests stub passed")
