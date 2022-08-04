N = int(input())
A = list(map(int,input().split()))

d = dict()
for i in range(N):
    if A[i] in d:
        d[A[i]] += 1
    else:
        d[A[i]] = 1

b2 = []
b4 = []
for a in d.keys():
    if d[a] >= 4:
        b4.append(a)
        b2.append(a)
    elif d[a] >= 2:
        b2.append(a)

b4.sort()
b2.sort()
s2 = 0
s4 = 0
if len(b4) >= 1:
    s4 = b4[-1]**2
if len(b2) >= 2:
    s2 = b2[-1]*b2[-2]

print(max(s4,s2))


#2022/7/15 00:13:02 1WA