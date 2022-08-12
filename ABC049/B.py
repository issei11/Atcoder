H,W = map(int,input().split())
C = [input() for _ in range(H)]
ans = []
for i in range(2*H):
    print(C[i//2])
#2022/8/12 00:03:43