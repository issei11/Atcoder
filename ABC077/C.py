import bisect
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort()
B.sort()
C.sort()

ans = 0
a = [0 for _ in range(N)]
b = [0 for _ in range(N)]
s = [0 for _ in range(N)]
tmp = 0
for i in range(N):
    a[i] = N-bisect.bisect_right(B,A[i])
    b[i] = N-bisect.bisect_right(C,B[i])

for i in range(1,N+1):
    s[-i] = b[-i] + tmp
    tmp = s[-i]


for i in range(N):
    if a[i] == 0:
        continue
    ans += s[N-a[i]]
print(ans)

#2022/8/29 00:26:17