N,K,Q = map(int,input().split())
A = list(map(int,input().split()))
L = list(map(int,input().split()))

grid = [0 for _ in range(N+1)]

for a in A:
    grid[a] += 1

for x in L:
    l = x-1
    if A[l] != N:
        if grid[A[l]+1] == 0:
            grid[A[l]] = 0
            grid[A[l]+1] += 1
            A[l] += 1

ans = []
for i in range(N+1):
    if grid[i] == 1:
        ans.append(i)
print(*ans)