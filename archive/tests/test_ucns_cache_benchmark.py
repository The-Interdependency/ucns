from scripts.bench_ucns_cache import fixtures, run


def test_benchmark_workload_uses_domain_catalogue_objects():
    objs = fixtures()
    assert len(objs) == 50
    assert all(obj is not None for obj in objs)


def test_benchmark_workload_exercises_structural_hits_without_speedup_claim():
    metrics = run()
    assert metrics["total_calls"] == 50
    assert metrics["structural_hits"] > 0
    assert metrics["time_saved"] is None
