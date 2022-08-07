L,H = map(int,input().split())
N = int(input())
for _ in range(N):
    A = int(input())
    if A < L:
        print(L-A)
    elif A > H:
        print(-1)
    else:
        print(0)
#2022/8/7 00:03:24