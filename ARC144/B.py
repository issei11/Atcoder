N, a, b = map(int,input().split())
A = list(map(int,input().split()))

M1 = 0
M2 = 0
m1 = 10**9+1
m2 = 10**9+1

for a in A:
    if a > M1:
        M2 = M1
        M1 = a
    elif a > M2:
        M2 = a
    if m1 < a:
        m2 = m1
        m1 = a
    elif m2 < a:
        m2 = a

m = 0
while True:
    m = min(m1+a,m2,M1-b)
    if m < m1:
        break
    else:
        

print(m1)