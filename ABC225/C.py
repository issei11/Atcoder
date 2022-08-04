N,M = map(int,input().split())
B = [[0]*(M+1)]
for i in range(N):
    B_i = [0]+list(map(int,input().split()))
    B.append(B_i)

cnt = 1

if B[1][1]%7 == 0 and M != 1:
    cnt -= 1

for j in range(2,M+1):
    if B[1][j] == B[1][j-1]+1:
        cnt += 1
    if B[1][j]%7 == 0 and j != M:
        cnt -= 1

for i in range(2,N+1):
    if B[i][1] == B[i-1][1]+7:
        cnt += 1

for i in range(2,N+1):
    for j in range(2,M+1):
        if B[i][j] == B[i][j-1]+1 and B[i][j] == B[i-1][j]+7:
            cnt += 1
        if B[i][j]%7 == 0 and j != M:
            cnt -= 1

print('Yes' if cnt == N*M else 'No')

#2022/5/6 00:43:57