import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(__file__))

import streamlit as st
from collections import Counter
from sampler import RandomWeightedSampler
import pandas as pd

st.title("Weighted Random Sampler - Interactive Demo")
st.write("Enter items, one per line, like: apple,1")
raw =  st.text_area("Items", "apples,1\nbanana,2\ncherry,7")
lines = [l.strip() for l in raw.splitlines() if l.strip()]
items = []
for l in lines:
    try:
        name, w = l.split(",")
        items.append((name.strip(),float(w)))
    except Exception:
        st.error(f"Invalid line: {l}")


method = st.selectbox("Method", ["prefix_sum"])
total_weight = sum(weight for _, weight in items)
if items:
    st.write("**Total Weight:**", total_weight)
    st.write("**Initial Probability**")
    for name, weight in items:
        proba = weight/total_weight
        st.write(f"- {name}: {proba:.3f}       ({weight}/{total_weight})")
initial_n = len(items) if items else 1
n = st.number_input("Number of samples", min_value=1, value=initial_n, step=1)

if st.button("Run") and items:
    if method == "prefix_sum":
        sampler = RandomWeightedSampler(items)
    samples = sampler.sample_multiple(n)
    counts = Counter(samples)
    df = pd.DataFrame([(k,v,v/n) for k, v in counts.items()],
    columns = ["item", "count", "frequency"]).sort_values("frequency", ascending=False)
    st.table(df.set_index("item"))
    st.bar_chart(df.set_index("item")["frequency"])
