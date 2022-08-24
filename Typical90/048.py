N,K = map(int,input().split())
A = []
B = []
A_B = []
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    A_B.append(a-b)

#2022/8/24 00:14:43