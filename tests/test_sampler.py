import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from collections import Counter
from sampler import RandomWeightedSampler


def test():
    items = [("a",1), ("b",2), ("c",7)]
    sampler = RandomWeightedSampler(items)
    samples = sampler.sample_multiple(10000)
    counts = Counter(samples)
    total = sum(counts.values())
    assert abs(counts["a"]/total-0.1) < 0.03
    assert abs(counts["b"]/total-0.2) < 0.03
    assert abs(counts["c"]/total-0.7) < 0.03

