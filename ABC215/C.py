from itertools import permutations
S,K = input().split()
K = int(K)
l = set()
for i in permutations(S):
    l.add("".join(i))
l = sorted(l)
print(l[K-1])
#2022/5/17 00:07:27