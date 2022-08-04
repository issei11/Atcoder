P = []
for a in range(1,200):
    for b in range(1,200):
        P.append(4*a*b+3*a+3*b)
P.sort()

N = int(input())
S = list(map(int,input().split()))

cnt = 0
for s in S:
    for p in P:
        if s == p:
            cnt += 1
            break

print(len(S)-cnt)
#2022/5/4 0:06:44