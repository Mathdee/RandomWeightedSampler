# Random Weighted Sampler

A high-performance Python implementation of weighted random sampling using prefix sums and binary search.

## Overview

This project demonstrates efficient weighted random sampling - a technique for selecting items from a collection where each item has a different probability of being chosen based on its assigned weight. Items with higher weights are more likely to be selected.

### Problem Solved
- **Weighted Selection**: Choose items with probabilities proportional to their weights
- **Efficiency**: O(log n) time complexity per sample using binary search
- **Accuracy**: Precise probability distribution matching theoretical expectations

## Features

- **Fast Sampling**: O(log n) time complexity per sample
- **Memory Efficient**: O(n) space complexity for initialization
- **Interactive Demo**: Streamlit web app for experimentation
- **Visual Analysis**: Matplotlib plots comparing expected vs observed frequencies
- **Comprehensive Testing**: Unit tests with pytest
- **Easy to Use**: Simple API with clear documentation

## Algorithm

The implementation uses a **prefix sum array** combined with **binary search**:

1. **Initialization**: Build a prefix sum array from the weights
2. **Sampling**: Generate a random number and use binary search to find the corresponding item
3. **Efficiency**: Binary search provides O(log n) lookup time

### Visual Representation

```
Items: [("apple", 1), ("banana", 2), ("cherry", 7)]
Weights: [1, 2, 7]
Prefix Sums: [1, 3, 10]

Random number: 0.0 - 1.0 → apple
Random number: 1.0 - 3.0 → banana  
Random number: 3.0 - 10.0 → cherry
```

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd Week1
```

2. **Create virtual environment** (Windows)
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. **Create virtual environment** (macOS/Linux)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Basic Example

```python
from sampler import RandomWeightedSampler

# Define items with weights
items = [("apple", 1), ("banana", 2), ("cherry", 7)]

# Create sampler
sampler = RandomWeightedSampler(items)

# Sample single item
sample = sampler.sample()
print(f"Selected: {sample}")  # Output: cherry (most likely)

# Sample multiple items
samples = sampler.sample_multiple(1000)
print(f"Sample count: {len(samples)}")
```

### Advanced Example

```python
from collections import Counter
from sampler import RandomWeightedSampler

# More complex data
items = [
    ("rare_item", 1),
    ("common_item", 10),
    ("legendary_item", 0.1)
]

sampler = RandomWeightedSampler(items)
samples = sampler.sample_multiple(10000)

# Analyze results
counts = Counter(samples)
total = len(samples)

for item, count in counts.items():
    frequency = count / total
    print(f"{item}: {frequency:.3f} ({count}/{total})")
```

**Expected Output:**
```
common_item: 0.901 (9010/10000)
rare_item: 0.090 (900/10000)
legendary_item: 0.009 (90/10000)
```

## Running the Code



### Run Demo Plots
```bash
python notebooks/demo.py
```
This generates matplotlib plots comparing expected vs observed frequencies.

### Run Interactive Demo
```bash
streamlit run demo/app.py
```
This launches a web interface where you can:
- Add custom items and weights
- Adjust sample size (input integer)
- View real-time frequency analysis
- See interactive bar charts

## 📊 Performance

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Initialization | O(n) | O(n) |
| Single Sample | O(log n) | O(1) |
| Multiple Samples | O(k log n) | O(1) |

Where:
- n = number of items
- k = number of samples requested



## Testing

The project includes comprehensive unit tests:

```bash
pytest -q
```

Tests cover:
- Basic functionality
- Edge cases (single item, zero weights)
- Probability distribution accuracy
- Performance benchmarks

## Project Structure

```
Week1/
├── sampler.py              # Main implementation
├── demo/
│   └── app.py             # Streamlit web app
├── notebooks/
│   └── demo.py            # Matplotlib visualization
├── tests/
│   └── test_sampler.py    # Unit tests
├── requirements.txt       # Dependencies
└── README.md             # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Improvements

- [ ] Additional sampling algorithms (alias method, reservoir sampling)
- [ ] Performance benchmarks vs other libraries
- [ ] Support for dynamic weight updates
- [ ] Multi-threaded sampling
- [ ] Integration with popular ML libraries

## References

- [Weighted Random Sampling](https://en.wikipedia.org/wiki/Reservoir_sampling#Weighted_Random_Sampling)
- [Binary Search Algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm)
- [Prefix Sum Arrays](https://en.wikipedia.org/wiki/Prefix_sum)

---

