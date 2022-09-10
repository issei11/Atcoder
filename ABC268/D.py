from itertools import permutations
from itertools import combinations_with_replacement

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
S = [input()[:-1] for _ in range(N)]
T = set([input()[:-1] for _ in range(M)])
if N == 1 and len(S[0]) < 3:
    print(-1)
    exit()
buf = 16-N+1
for i in range(N):
    buf -= len(S[i])

under_list = [1 for _ in range(N)]
X = []
for p in combinations_with_replacement(range(N), buf):
    for pi in p:
        under_list[pi] += 1
    for a in permutations(range(N)):
        for j in range(N-1):  
            X.append(S[a[j]])
            for k in range(under_list[j]):
                X.append('_')
        X.append(S[a[N-1]])
        output = "".join(X)
        if output not in T:
            print(output)
            exit()
        X = []     
    under_list = [1 for _ in range(N)]
print(-1)