# Triangle, pentagonal, and hexagonal numbers are generated by the following
# formulae:
# Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
# Pentagonal      Pn=n(3n-1)/2        1, 5, 12, 22, 35, ...
# Hexagonal       Hn=n(2n-1)      1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
# Find the next triangle number that is also pentagonal and hexagonal.


n = 143
flag = True
while flag:
    n += 1
    H = n*((2*n) - 1)
    P = (1 + (1 + (24*H))**0.5) / 6.0
    if P == int(P):
        T = (-1 + (1 + (8*H))**0.5) / 2.0
        if T == int(T):
            print ("n = %d\nT = %d\nP = %d\nH = %d" %(n, T*(T+1)/2, P*(3*P-1)/2, H))
            flag = False
            break
# 1533776805