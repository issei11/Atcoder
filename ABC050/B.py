N = int(input())
T = list(map(int,input().split()))
M = int(input())
ans = sum(T)
for _ in range(M):
    p,x = map(int,input().split())
    print(ans - (T[p-1]-x))
#2022/8/12 00:03:06