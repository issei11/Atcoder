from itertools import combinations

N,M = map(int,input().split())
for comb in combinations(range(1,M+1),N):
    print(*comb)