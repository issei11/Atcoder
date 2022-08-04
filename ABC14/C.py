n = int(input())
A = [0 for _ in range(1000001)]
B = [0 for _ in range(1000001)]
for _ in range(n):
    a,b = map(int,input().split())
    A[a] += 1
    B[b] += 1

A_cnt = 0
B_cnt = 0
ans = [0 for _ in range(1000001)]
for i in range(1000001):
    A_cnt += A[i]
    ans[i] = A_cnt - B_cnt
    B_cnt += B[i]
print(max(ans))
#2022/8/2 00:13:46