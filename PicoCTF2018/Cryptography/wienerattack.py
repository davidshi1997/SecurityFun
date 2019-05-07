import sys, hashlib
from sympy import *

e = 23964026063100941803015063930230162623973323387139268312605842804459066777958872885000348102930543732721011438908984769930034418025303319270449442058456558910273662347986052507708183592570160073560834882189580093972401559919866847166305616709210146843290907871347541024837710909478200081170867014192312628193
n = 128563390315770008426997236803822377855872601082428473101117314986561383384666883780637509301060825524831117114585636449484664837436501607320517770480113603494968369554273065890275697688598199977124916003115666382611124848136912491958121367219038083130056171444258958103165256228915650826733626941385046180177


def cf_expansion(n, d):
    e = []

    q = n // d
    r = n % d
    e.append(q)

    while r != 0:
        n, d = d, r
        q = n // d
        r = n % d
        e.append(q)

    return e

def convergents(e):
    n = [] # Nominators
    d = [] # Denominators

    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else: # i > 1
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]

        n.append(ni)
        d.append(di)
        yield (ni, di)

def weiner_attack(convergent):
    for pk, pd in convergent:
        if pk == 0:
            continue;
        possible_phi = (e*pd - 1)//pk 
        p = Symbol('p', integer=True)
        roots = solve(p**2 + (possible_phi - n - 1)*p + n, p)
        if len(roots) == 2:
            print('Wiener\'s Attack succeeded!')
            return pd
    print('Wiener\'s Attack failed... Could not factor N')
    return -1

def main():
    expansion = cf_expansion(e, n)
    convergent = convergents(expansion)
    result = weiner_attack(convergent)

    print(result)
    
main()