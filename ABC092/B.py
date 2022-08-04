N = int(input())
D,X = map(int,input().split())
ans = X
for _ in range(N):
    A = int(input())
    ans += (D-1)//A+1
print(ans)
#2022/7/20 00:05:04