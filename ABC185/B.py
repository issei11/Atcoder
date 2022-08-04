N, M, T = map(int,input().split())
storage = N
B1 = 0
for _ in range(M):
    A,B = map(int,input().split())
    storage -= A-B1
    if storage <= 0:
        break
    storage = min(N,storage+B-A)
    B1 = B

storage -= T-B1

print("Yes" if storage > 0 else "No")
#2022/6/8 00:13:20