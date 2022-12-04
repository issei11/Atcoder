N = int(input())
S = list(map(int,input().split()))
A = [S[0]]
tmp = S[0]
for i in range(1,N):
    A.append(S[i]-tmp)
    tmp = S[i]
print(*A)