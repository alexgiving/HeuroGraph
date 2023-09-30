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
          Instance  Time, s  Clique size
        C125.9.clq     0.00           26
    brock200_3.clq     0.00           10
    brock400_4.clq     0.00           16
  johnson8-2-4.clq     0.00            4
    p_hat300-3.clq     0.00           15
      MANN_a27.clq     0.00           39
    brock200_4.clq     0.00           12
gen200_p0.9_44.clq     0.00           27
       keller4.clq     0.00            9
    p_hat500-3.clq     0.00           28
       MANN_a9.clq     0.00           12
    brock400_1.clq     0.00           15
gen200_p0.9_55.clq     0.00           29
   p_hat1000-1.clq     0.00            5
       san1000.clq     0.01            7
    brock200_1.clq     0.00           14
    brock400_2.clq     0.00           16
    hamming8-4.clq     0.00           16
   p_hat1000-2.clq     0.01           21
   sanr200_0.9.clq     0.00           27
    brock200_2.clq     0.00            7
    brock400_3.clq     0.00           16
 johnson16-2-4.clq     0.00            8
   p_hat1500-1.clq     0.01            6
   sanr400_0.7.clq     0.00           13
```
