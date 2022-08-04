from itertools import product

N,K = map(int,input().split())
T = []
for _ in range(N):
    t = list(map(int,input().split()))
    T.append(t)

for pro in product(range(K),repeat=N):
    result = T[0][pro[0]]
    for i in range(1,N):
        result = result ^ T[i][pro[i]]
    if result == 0:
        print('Found')
        exit()
print('Nothing')
#2022/8/2 00:28:53