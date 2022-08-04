import sys
sys.setrecursionlimit(40000)

def dfs(numQ,value):
    if numQ == N:
        return value == 0
    for i in range(K):
        if dfs(numQ+1,value^T[numQ][i]):
            return True
    return False

N,K = map(int,input().split())
T = []
for _ in range(N):
    t = list(map(int,input().split()))
    T.append(t)
print('Found' if dfs(0,0) else 'Nothing')