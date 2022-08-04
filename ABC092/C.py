N = int(input())
A = [0]+list(map(int,input().split()))

s = 0
for i in range(N):
    s += abs(A[i+1]-A[i])
s += abs(A[0]-A[N])

for i in range(N-1):
    s_ans = s-abs(A[i+1]-A[i])-abs(A[i+2]-A[i+1])+abs(A[i+2]-A[i])
    print(s_ans)

s_ans = s-abs(A[N]-A[N-1])-abs(A[0]-A[N])+abs(A[0]-A[N-1])
print(s_ans)
#2022/7/20 00:10:44