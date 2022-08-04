n = int(input())
a = list(map(int,input().split()))
b = []
if n%2 == 0:
    for i in range(n//2):
        b.append(a[n-1-i*2])
    for i in range(n//2):
        b.append(a[i*2])
else:
    for i in range(n//2+1):
        b.append(a[n-1-i*2])
    for i in range(n//2):
        b.append(a[2*i+1])
print(*b)
#2022/6/12 00:09:12