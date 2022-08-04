N = int(input())
S = [0] + list(map(int,input().split()))
T = [0] + list(map(int,input().split()))

S_sum = [0]
s = 0
for i in range(1,N+1):
    s += S[i]
    S_sum.append(s)

for n in range(1,N+1):
