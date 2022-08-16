N,Q,X = map(int,input().split())
W = list(map(int,input().split()))

acc = []
s = 0
for w in W:
    s += w
    acc.append(s)

check = [0 for _ in range(N)]
check[0] = 1




#for _ in range(Q):
#    K = int(input())
