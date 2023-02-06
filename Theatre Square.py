from math import ceil
n,m,a = map(int,input().split())

if n < a and m < a:
    print(1)
else:
    dn = ceil(n / a)
    dm = ceil(m / a)
    print(dn)
    print(dn*dm)
