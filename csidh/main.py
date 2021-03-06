from framework import *

if setting.style == 'wd1':
    # Using one torsion point and dummy isogeny constructions
    from csidh.gae_wd1 import *
    delta = 1
elif setting.style == 'wd2':
    # Using two torsion points and dummy isogeny constructions
    from csidh.gae_wd2 import *
    delta = 2
elif setting.style == 'df':
    # Dummy-free approach by using two torsion points
    from csidh.gae_df import *
    delta = 1
else:

    print("  ,-~~-.___.          ")
    print(" / |  '     \\          SYNTAX ERROR ..., run python3 main.py -h for help") 
    print("(  )         0        ")  
    print(" \_/-, ,----'         ")         
    print("    ====           // ")
    print("   /  \-'~;    /~~~(O)")
    print("  /  __/~|   /       |")   
    print("=(  _____| (_________|")
    exit(7)

''' -------------------------------------------------------------------------------------
    Number of degree-(l_i) isogeny constructions to be performed: m_i
    ------------------------------------------------------------------------------------- '''

# ==========================================================================

if( setting.prime == 'p512' ):                                                                                                                                                                                                                
                                                                                                                                                                                                                                            
    if(setting.style == 'wd1'):                                                                                                                                                                                                                      
        # ====== [MCR style, CSIDH-512] each m_i corresponds with the given in MCR18                                                                                                                                                        
        #m = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5]                                                                                                                                                                                               
                                                                                                                                                                                                                                            
        # ===== Suitable bounds for this work                                                                                                                                                                                               
        m = [15, 18, 20, 21, 21, 22, 22, 22, 22, 22, 22, 19, 20, 22, 23, 23, 23, 23, 23, 23, 23, 21, 23, 20, 16, 16, 16, 15, 14, 12, 13, 12, 11, 11, 10, 10, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3]

        # ====== [MCR style, CSIDH-512] case when each m_i is equal to 10, and it implies a key space of (10 + 1)^74 ~ 2^256 ~ p^1/4
        #m = [10] * n
        
        #sigma, kappa = 1, 10 # when only one strategy is required; that is, m = (10, 10, ..., 10)
        sigma, kappa = 5, 11 # MCR & dummy-free [The given one in MCR18] CSIDH-512
    
    if(setting.style == 'wd2'):
        # ====== [OAYT style, CSIDH-512] each m_i corresponds with the given in OAYT19
        #m = [5, 6, 7, 7, 7, 7, 7, 8, 8, 8, 9, 10, 10, 10, 10, 9, 9, 9, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1]

        # ===== Suitable bounds for this work
        m = [7, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 9, 11, 9, 8, 8, 8, 7, 7, 7, 7, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]

        # ====== [OAYT style, CSIDH-512] case when each m_i is equal to 5, and it implies a key space of (2*5 + 1)^74 ~ 2^256 ~ p^1/4
        #m = [5] * n
        
        #sigma, kappa = 1, 5 # when only one strategy is required; that is, m = (5, 5, ..., 5)
        sigma, kappa = 3, 8 # OAYT [The given one in OAYT19] CSIDH-512
    
    if(setting.style == 'df'):
        # ====== [dummy-free style, CSIDH-512] each m_i corresponds with the given in MCR18 (it is the same as MCR style)
        #m = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5]

        # ===== Suitable bounds for this work
        m = [15, 18, 20, 21, 21, 22, 22, 22, 22, 22, 22, 19, 20, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 19, 16, 16, 16, 15, 14, 12, 13, 12, 11, 11, 11, 9, 9, 9, 9, 8, 8, 8, 8, 7, 8, 6, 6, 6, 6, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3]

        # ====== [dummy-free style, CSIDH-512] case when each m_i is equal to 10, and it implies a key space of (10 + 1)^74 ~ 2^256 ~ p^1/4
        #m = [10] * n
        
        #sigma, kappa = 1, 10 # when only one strategy is required; that is, m = (10, 10, ..., 10)
        sigma, kappa = 5, 11 # MCR & dummy-free [The given one in MCR18] CSIDH-512

elif( setting.prime == 'p1024'):
    # Ths branch corresponds with the proposal CSIDH-1024 of https://csidh.isogeny.org/index.html
    # Simba parameters should be optimized(?)

    if(setting.style == 'wd1'):

        # ===== MCR style (key-space size is 4^130 = 2^260 >= 2^256)
        #m = [3] * n

        # ===== Suitable bounds for this work
        m = [4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        sigma, kappa = 5, 4

    if(setting.style == 'wd2'):

        # ===== OAYT style (using the proposal bounds given in https://csidh.isogeny.org/index.html)
        #m = [2] * n
        
        # ===== Suitable bounds for this work
        m = [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        sigma, kappa = 3, 5

    if(setting.style == 'df'):

        # ===== dummy-free style (key-space size is 4^130 = 2^260 >= 2^256)
        #m = [3] * n

        # ===== Suitable bounds for this work
        m = [4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        sigma, kappa = 5, 4

elif( setting.prime == 'p1792'):
    # Ths branch corresponds with the proposal CSIDH-1024 of https://csidh.isogeny.org/index.html
    # Simba parameters should be optimized(?)

    if(setting.style == 'wd1'):

        # ===== MCR style (key-space size is 3^207 > 2^256)
        #m = [2] * n

        # ===== Suitable bounds for this work
        m = [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        sigma, kappa = 5, 4

    if(setting.style == 'wd2'):

        # ===== OAYT style (using the proposal bounds given in https://csidh.isogeny.org/index.html)
        m = [1] * n
        
        # ===== Suitable bounds for this work
        sigma, kappa = 3, 5

    if(setting.style == 'df'):

        # ===== dummy-free style (key-space size is 3^207 > 2^256)
        #m = [2] * n

        # ===== Suitable bounds for this work
        m = [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        sigma, kappa = 5, 4

else:
    print("[ERROR]\tMissing bound. To set the maximum number of isogeny constructions, and sigma and kappa from SIMBA method (to add they in ELSE statement in line 147 of file csidh.py)")
    exit(11)

# ==========================================================================

if len(set(m)) > 1:
    # Maximum number of degree-(l_i) isogeny constructions is m_i (different for each l_i)
    LABEL_m = 'different_bounds'
else:
    # Maximum number of degree-(l_i) isogeny constructions is m (the same for each l_i)
    LABEL_m = 'with_same_bounds'

if setting.verbose:
    verb = '-suitable'
else:
    verb = '-classical'

try:

    # List of Small Odd Primes, L := [l_0, ..., l_{n-1}]
    m_prime = [ geometric_serie(m[k], L[k]) for k in range(n) ]
    r_out, L_out, R_out = rounds(m_prime[::-1], n)
    for j in range(0, len(r_out), 1):

        R_out[j] = list([L[::-1][k] for k in R_out[j]])
        L_out[j] = list([L[::-1][k] for k in L_out[j]])

    f = open('./strategies/' + setting.algorithm + '-' + setting.prime  + '-' + setting.style + '-' + setting.formulaes + '-' + LABEL_m + verb)
    print("// Strategies to be read from a file")
    S_out = []
    for i in range(0, len(r_out), 1):

        tmp = f.readline()
        tmp = [ int(b) for b in tmp.split() ]
        S_out.append(tmp)

    f.close()

except IOError:

    print("// Strategies to be computed")
    C_out, L_out, R_out, S_out, r_out = strategy_block_cost(L[::-1], m[::-1])
    f = open('./strategies/' + setting.algorithm + '-' + setting.prime  + '-' + setting.style + '-' + setting.formulaes + '-' + LABEL_m + verb,'w')
    for i in range(0, len(r_out)):

        f.writelines(' '.join([ str(tmp) for tmp in S_out[i]]) + '\n')

    f.close()

print("// All the experiments are assuming S = %1.6f x M and a = %1.6f x M. The measures are given in millions of field operations.\n" % (SQR, ADD))


''' -------------------------------------------------------------------------------------
    Framework
    ------------------------------------------------------------------------------------- '''
    
print("p := 0x%X;" % p)
print("fp := GF(p);")
print("P<x> := PolynomialRing(fp);");
print("fp2<i> := ext<fp | x^2 + 1>;")
print("P<x> := PolynomialRing(fp2);");

A = [2, 4]
print("public_coeff := 0x%X;\n" % coeff(A))

''' -------------------------------------------------------------------------------------
    Main
    ------------------------------------------------------------------------------------- '''

print("// Maximum number of degree-(\ell_i) isogeny constructions: m_i")
print("/*")
printl("m", m, n // 3)
print("*/")
print("// ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("// Public Key Generation")
print("// ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

temporal_m = list(set(m))
T_p, T_m = full_torsion_points(A)

# ------------------------------------------------------------------------- Alice
set_zero_ops()
public_validation = validate(A)
assert(public_validation)

a_private = random_key(m)
print("// Private key corresponding to Alice")
print("/*")
printl("sk_a", a_private, n // 3)
print("*/")

RUNNING_TIME = get_ops()
print("// Public key corresponding to Alice")
print("// public key validation cost  :\t%2.3fM + %2.3fS + %2.3fa = %2.3fM," % (RUNNING_TIME[0] / (10.0**6), RUNNING_TIME[1] / (10.0**6), RUNNING_TIME[2] / (10.0**6), measure(RUNNING_TIME) / (10.0**6)) )

set_zero_ops()
if len(temporal_m) == 1:
    if temporal_m[0] > 1:
        a_public = GAE(A, a_private, [L_out[0]], [ [] ], [S_out[0]], temporal_m, m)
    else:
        if setting.style == 'wd1':
            # ONE torsion  point required
            a_public, m_tmp, a_tmp = evaluate_strategy(A, T_p, L_out[0], S_out[0], n, m, a_private)
        else:
            # TWO torsion points required
            a_public, m_tmp, a_tmp = evaluate_strategy(A, list([list(T_m), list(T_p)]), L_out[0], S_out[0], n, m, a_private)
else:
    a_public = GAE(A, a_private, L_out, R_out, S_out, r_out, m)
    
RUNNING_TIME = get_ops()
print("// group action evaluation cost:\t%2.3fM + %2.3fS + %2.3fa = %2.3fM;" % (RUNNING_TIME[0] / (10.0**6), RUNNING_TIME[1] / (10.0**6), RUNNING_TIME[2] / (10.0**6), measure(RUNNING_TIME) / (10.0**6)) )
print("pk_a := 0x%X;\n" % coeff(a_public))

# ------------------------------------------------------------------------- Bob
set_zero_ops()

b_private = random_key(m)
print("// Private key corresponding to Bob")
print("/*")
printl("sk_b", b_private, n // 3)
print("*/")

set_zero_ops()
public_validation = validate(A)
assert(public_validation)
RUNNING_TIME = get_ops()
print("// Public key corresponding to Bob")
print("// public key validation cost  :\t%2.3fM + %2.3fS + %2.3fa = %2.3fM," % (RUNNING_TIME[0] / (10.0**6), RUNNING_TIME[1] / (10.0**6), RUNNING_TIME[2] / (10.0**6), measure(RUNNING_TIME) / (10.0**6)) )

set_zero_ops()
if len(temporal_m) == 1:
    if temporal_m[0] > 1:
        b_public = GAE(A, b_private, [L_out[0]], [ [] ], [S_out[0]], temporal_m, m)
    else:
        if setting.style == 'wd1':
            # ONE torsion  point required
            b_public, m_tmp, b_tmp = evaluate_strategy(A, T_p, L_out[0], S_out[0], n, m, b_private)
        else:
            # TWO torsion points required
            b_public, m_tmp, b_tmp = evaluate_strategy(A, list([list(T_m), list(T_p)]), L_out[0], S_out[0], n, m, b_private)
else:
    b_public = GAE(A, b_private, L_out, R_out, S_out, r_out, m)
    
RUNNING_TIME = get_ops()
print("// group action evaluation cost:\t%2.3fM + %2.3fS + %2.3fa = %2.3fM;" % (RUNNING_TIME[0] / (10.0**6), RUNNING_TIME[1] / (10.0**6), RUNNING_TIME[2] / (10.0**6), measure(RUNNING_TIME) / (10.0**6)) )
print("pk_b := 0x%X;" % coeff(b_public))

print("\n// ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("// Secret Sharing Computation")
print("// ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# ------------------------------------------------------------------------- Alice
set_zero_ops()
public_validation = validate(b_public)
assert(public_validation)
RUNNING_TIME = get_ops()
print("// Secret sharing corresponding to Alice")
print("// public key validation cost  :\t%2.3fM + %2.3fS + %2.3fa = %2.3fM," % (RUNNING_TIME[0] / (10.0**6), RUNNING_TIME[1] / (10.0**6), RUNNING_TIME[2] / (10.0**6), measure(RUNNING_TIME) / (10.0**6)) )

Tp_b, Tm_b = full_torsion_points(b_public)
set_zero_ops()
if len(temporal_m) == 1:
    if temporal_m[0] > 1:
        ss_a = GAE(b_public, a_private, [L_out[0]], [ [] ], [S_out[0]], temporal_m, m)
    else:
        if setting.style == 'wd1':
            # ONE torsion  point required
            ss_a, m_tmp, a_tmp = evaluate_strategy(b_public, Tp_b, L_out[0], S_out[0], n, m, a_private)
        else:
            # TWO torsion points required
            ss_a, m_tmp, a_tmp = evaluate_strategy(b_public, list([list(Tm_b), list(Tp_b)]), L_out[0], S_out[0], n, m, a_private)
else:
    ss_a = GAE(b_public, a_private, L_out, R_out, S_out, r_out, m)
    
RUNNING_TIME = get_ops()

print("// group action evaluation cost:\t%2.3fM + %2.3fS + %2.3fa = %2.3fM;" % (RUNNING_TIME[0] / (10.0**6), RUNNING_TIME[1] / (10.0**6), RUNNING_TIME[2] / (10.0**6), measure(RUNNING_TIME) / (10.0**6)) )
print("ss_a := 0x%X;\n" % coeff(ss_a))

# ------------------------------------------------------------------------- Bob
set_zero_ops()
public_validation = validate(a_public)
assert(public_validation)
RUNNING_TIME = get_ops()
print("// Secret sharing corresponding to Bob")
print("// public key validation cost  :\t%2.3fM + %2.3fS + %2.3fa = %2.3fM," % (RUNNING_TIME[0] / (10.0**6), RUNNING_TIME[1] / (10.0**6), RUNNING_TIME[2] / (10.0**6), measure(RUNNING_TIME) / (10.0**6)) )

Tp_a, Tm_a = full_torsion_points(a_public)
set_zero_ops()
if len(temporal_m) == 1:
    if temporal_m[0] > 1:
        ss_b = GAE(a_public, b_private, [L_out[0]], [ [] ], [S_out[0]], temporal_m, m)
    else:
        if setting.style == 'wd1':
            # ONE torsion  point required
            ss_b, m_tmp, b_tmp = evaluate_strategy(a_public, Tp_a, L_out[0], S_out[0], n, m, b_private)
        else:
            # TWO torsion points required
            ss_b, m_tmp, b_tmp = evaluate_strategy(a_public, list([list(Tm_a), list(Tp_a)]), L_out[0], S_out[0], n, m, b_private)
else:
    ss_b = GAE(a_public, b_private, L_out, R_out, S_out, r_out, m)
    
RUNNING_TIME = get_ops()
print("// group action evaluation cost:\t%2.3fM + %2.3fS + %2.3fa = %2.3fM;" % (RUNNING_TIME[0] / (10.0**6), RUNNING_TIME[1] / (10.0**6), RUNNING_TIME[2] / (10.0**6), measure(RUNNING_TIME) / (10.0**6)) )
print("ss_b := 0x%X;\n" % coeff(ss_b))


print("\n// ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
if( coeff(ss_a) == coeff(ss_b) ):
    print('\x1b[0;30;43m' + '\"Successfully passed!\";' + '\x1b[0m')
else:
    print('\x1b[0;30;41m' + '\"Great Scott!... The sky is falling. NOT PASSED!!!\"' + '\x1b[0m')

