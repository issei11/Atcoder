N = int(input())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

t = [A[i]/B[i] for i in range(N)]

t_sum = sum(t)
tmp = 0
i = 0
while tmp <= t_sum/2:
    tmp += t[i]
    i += 1

print(sum(A[:i])-(tmp-t_sum/2)*B[i-1])
#2022/5/7 00:15:42