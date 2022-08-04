H,W,C,Q = map(int,input().split())
ans = [0 for _ in range(C)]
h_sum = 0
w_sum = 0
t = []
n = []
n_set1 = set()
n_set2 = set()
c = []
for _ in range(Q):
    T,N,C = map(int,input().split())
    t.append(T)
    n.append(N)
    c.append(C)

for i in range(1,Q+1):
    if t[-i] == 1:
        if n[-i] in n_set1:
            n[-i] = 0
        else:
            n_set1.add(n[-i])
    elif t[-i] == 2:
        if n[-i] in n_set2:
            n[-i] = 0
        else:
            n_set2.add(n[-i])

for i in range(1,Q+1):
    if t[-i] == 1:
        if n[-i] != 0:
            ans[c[-i]-1] += W-w_sum
            h_sum += 1
    elif t[-i] == 2:
        if n[-i] != 0:
            ans[c[-i]-1] += H-h_sum
            w_sum += 1
print(*ans)

#2022/7/19 00:45:56 1WA