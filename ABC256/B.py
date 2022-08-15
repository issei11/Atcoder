N = int(input())
A = list(map(int,input().split()))
P = 0
player = [0 for _ in range(N)]
for i in range(N):
    for j in range(i+1):
        player[j] += A[i]
for i in range(N):
    if player[i] >= 4:
        P += 1
print(P)