N = int(input())
P = [0]+list(map(int,input().split()))
Q = [0]*(N+1)
for i in range(1,N+1):
    Q[P[i]] = i
print(*Q[1:])
#2022/5/13 00:03:41