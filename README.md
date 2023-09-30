# Graph Heuristic Algorithms Library

## Installation
```bash
source ./venv/bin/activate
export PYTHONPATH=${PYTHONPATH}:$(pwd)
```

## Greedy Heuristic Vertex Coloring Solver

Get benchmark data
```bash
bash scripts/download_coloring.sh
```

Run evaluation script
```bash
python benchmark_coloring.py
```

### Result table
```text
       Instance  Time, s  Colors
    myciel3.col     0.00       4
    myciel7.col     0.01       8
    school1.col     0.05      31
school1_nsh.col     0.04      30
       anna.col     0.00      11
  miles1000.col     0.01      43
  miles1500.col     0.01      73
   le450_5a.col     0.04      11
  le450_15b.col     0.04      17
 queen11_11.col     0.00      15
```

## Greedy Randomized Clique Solver

Get benchmark data
```bash
bash scripts/download_clique.sh
```

Run evaluation script
```bash
python benchmark_clique.py
```

### Result table
```text
       Instance  Time, s  Colors
```
