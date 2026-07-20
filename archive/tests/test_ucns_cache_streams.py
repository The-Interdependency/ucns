from fractions import Fraction

from ucns import UCNSObject
from ucns_cache.braider import braid_streams
from ucns_cache.primitive_streams import derive_primitive_streams


def sample_obj():
    return UCNSObject(3, 3, [(Fraction(0), None), (Fraction(2, 3), None), (Fraction(4, 3), None)], [0, 1, 0])


def test_primitive_streams_equal_length():
    streams = derive_primitive_streams(sample_obj())
    assert len(streams.angle_bits) == len(streams.rotation_bits) == len(streams.chirality_bits) == streams.lcm_length


def test_braider_is_deterministic():
    streams = derive_primitive_streams(sample_obj())
    assert braid_streams(streams).lattice_hash == braid_streams(streams).lattice_hash
