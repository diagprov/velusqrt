# On the Velu's formulae and its applications to CSIDH and B-SIDH constant-time implementations


At a combined computational expense of about *6l* field operations, Velu's formulae are used to construct and evaluate degree-*l* isogenies in the vast majority of isogeny-based primitive implementations. Recently, Bernstein, de Feo, Leroux and Smith introduced an new approach for solving this same problem at a reduced cost of just *O(sqrt(l))* field operations. In this work, we present a concrete computational analysis of these novel formulae, along with several algorithmic tricks that helped us to slightly, but noticeably, reduce their practical cost.


## Compilation

The syntax compilation can be viewed by running one of the following three commands

```bash
# Corresponding with the key-exchange protocol
python3 main.py -h or python3 main.py --help
# Corresponding with benchmarking (only for CSIDH, which has a variable running-time cost independent from the key)
python3 main.py -h or python3 bench.py --help
# Corresponding with the costs of KPs (Kernel Point computation), xISOG (isogeny construction), and xEVAL (isogeny evaluation)
python3 main.py -h or python3 test.py --help
```

and any of the above commands should show:

```bash
usage: main.py [-h] -p PRIME -f FORMULAES -a ALGORITHM [-s STYLE] [-b BENCHMARK] [-v]

Parses command.

optional arguments:
  -h, --help            show this help message and exit
  -p PRIME, --prime PRIME
                        prime number configuration should be stored in pSUFFIX (sop folder is taken as default).
  -f FORMULAES, --formulaes FORMULAES
                        traditional (tvelu), sqrt (svelu), or hybrid (hvelu) velu formulaes to be used.
  -a ALGORITHM, --algorithm ALGORITHM
                        bsidh or csidh algorithm
  -s STYLE, --style STYLE
                        style to be used: wd1 (with dummy operations and a single torsion point), wd2 (with dummy operations and a two torsion point), or df (dummy-free approach).
  -b BENCHMARK, --benchmark BENCHMARK
                        number of experiments to be used in the benchmark.
  -v, --verbose         Verbose mode.
```

Notice, `csidh`  option requires the use of the flag `-s` (or `--style`). The verbose flag `-v` (or `--verbose`) requires to have stored the suitable parameters `#I`, `#J` and `#K` in the new velu's formulaes; in particular, let's assume we want those suitable parameters for a given prime `p`, then  one can store those parameters by running one of the following commands

```bash
# CSIDH
./autosearch.sh p csidh
sh autosearch.sh p csidh
bash autosearch.sh p csidh
# BSIDH
./autosearch.sh p bsidh
sh autosearch.sh p bsidh
bash autosearch.sh p bsidh
```

## Adding new primes

The field characteristic `p` should be stored in directory `sop/`, and CSIDH and BSIDH have different structures (see below):

```bash
# CSIDH format (here p = 2^c * l_1 * .... l_n - 1)
c l_1 l_2 ... l_n

# BSIDH format
Hexadecimal representation of the prime p
4 l_1 l_2 ... l_n
c e_1 e_2 ... e_n
l'_1 l'_2 ... l'_m
e'_1 e'_2 ... e'_m
```

For the case of BSIDH, `M := (4^c * l_1^{e_1} * l_2^{e_2} * ... * l_n^{e_n})` must divide `(p + 1)`, and `N := (l'_1^{e'_1} * l'_2^{e'_2} * ... * l'_n^{e'_n})` must divide `(p-1)`. Additionally, the order-`M` generators `PA`, `QA` and `PQA := PA - QA` should be stored in directory `gen/` as projective x-coordinate points. Similarly, the order-`N` generators `PB`, `QB` and `PQB := PB - QB` also should be stored it the same directory. Both 3-tuples of points must be stored in a single file with the following syntax:

```bash
Re(x(PA)) Im(x(PA)) Re(x(QA)) Im(x(QA)) Re(x(PQA)) Im(x(PQA))
Re(x(PB)) Im(x(PB)) Re(x(QB)) Im(x(QB)) Re(x(PQB)) Im(x(PQB))
```

where `Re(X)` and `Im(X)` denote the real and imaginary parts of X with respect to `F_p[i]/(i^2 + 1)`, respectively. Moreover, all the above twelve integers should be stored in hexadecimal."

## Examples

We summarize some examples of runs as follows

```bash
# CSIDH
python3 main.py -p p1024 -f tvelu -a csidh -s df
python3 main.py -p p512 -f svelu -a csidh -s wd2
python3 main.py -p p1792 -f hvelu -a csidh -s wd1 -v

python3 bench.py -p p512 -f hvelu -a csidh -s wd2 -b 1024 -v
python3 bench.py -p p512 -f hvelu -a csidh -s wd1 -b 1024 -v
python3 bench.py -p p512 -f hvelu -a csidh -s df -b 1024 -v

python3 test.py -p p1792 -f tvelu -a csidh
python3 test.py -p p1792 -f svelu -a csidh
python3 test.py -p p1792 -f hvelu -a csidh

# BSIDH
python3 main.py -p b6 -f tvelu -a bsidh
python3 main.py -p b5 -f svelu -a bsidh
python3 main.py -p b2 -f hvelu -a bsidh -v

python3 test.py -p b6 -f tvelu -a bsidh
python3 test.py -p b6 -f svelu -a bsidh
python3 test.py -p b6 -f hvelu -a bsidh

```

Remark, our implementation allows us to plot each optimal strategy required:

```bash
# CSIDH
python3 print-strategy.py -p p1024 -f tvelu -a csidh -s df
python3 print-strategy.py -p p512 -f svelu -a csidh -s wd2
python3 print-strategy.py -p p1792 -f hvelu -a csidh -s wd1 -v

# BSIDH
python3 print-strategy.py -p b6 -f tvelu -a bsidh
python3 print-strategy.py -p b5 -f svelu -a bsidh
python3 print-strategy.py -p b2 -f hvelu -a bsidh -v
```

Additionally, one can created files with extension `.h` that includes all the required variables in a the strategy evaluation (at least for CSIDH implementations).

```bash
# CSIDH
python3 header.py -p p512 -f tvelu -a csidh -s wd2
python3 header.py -p p1024 -f svelu -a csidh -s wd1 -v
python3 header.py -p p1792 -f hvelu -a csidh -s df -v
```

## Remarks

The primes labeled as `b2`, `b3`, `b5`, and `b6` correspond with the examples 2, 3, 5, and 6 of , respectively. In particular, we focused on primes such that `p = 3 mod 4`. Additionally, the product and squaring in `F_p[i]/(i^2 + 1)` were implemented using 3 and 2 products in `F_p`, respectively.

## Authors

1. **Gora Adj** <gora.adj@gmail.com,gora.adj@udl.cat>,
2. **_Jesús-Javier Chi-Domínguez_** <jesus.chidominguez@tuni.fi>, <chidoys@gmail.com>, <jjchi@computacion.cs.cinvestav.mx>, and
3. **_Francisco Rodríguez-Henríquez_** <francisco@cs.cinvestav.mx>.

## License

This project is licensed under the GNU general public license - see the [LICENSE](LICENSE) file for details

## Funding

This project has received funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (grant agreement No 804476). 

The third author received partial funds from the Mexican Science council CONACyT project 313572.