import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from collections import Counter
from sampler import RandomWeightedSampler
import matplotlib.pyplot as pt

items = [("apple",1), ("banana",2),("cherry", 7)]
n = 30000

p = RandomWeightedSampler(items)

p_samples = p.sample_multiple(n)
p_counts = Counter(p_samples)

labels = [it for it, _ in items]
expected = [w/sum(w for _, w in items)for _, w in items]
p_freq = [p_counts[l]/n for l in labels]

x = range(len(labels))
pt.figure(figsize=(9,4))
pt.subplot(1,2,1)
pt.bar(x, expected)
pt.xticks(x, labels)
pt.title("Expected probabalities")
pt.subplot(1,2,2)
pt.bar([i-0.2 for i in x], p_freq, width=0.4, label='prefix')
pt.xticks(x, labels)
pt.title("Observed Frequencies")
pt.show()
