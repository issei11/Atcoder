N,W = map(int,input().split())
A = list(map(int,input().split()))

tmp = 0
ans = set()
for a in A:
    if a <= W:
        ans.add(a)
for i in range(N):
    for j in range(i+1,N):
        tmp = A[i]+A[j]
        if tmp <= W:
            ans.add(tmp)
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            tmp = A[i]+A[j]+A[k]
            if tmp <= W:
                ans.add(tmp)
print(len(ans))