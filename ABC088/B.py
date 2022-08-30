N = int(input())
a = list(map(int,input().split()))
a = sorted(a,reverse=True)

A = 0
B = 0
for i in range(N):
    if i%2 == 0:
        A += a[i]
    else:
        B += a[i]
print(A-B)
#2022/8/31 00:02:43