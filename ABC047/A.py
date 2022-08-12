a = list(map(int,input().split()))
a.sort()
b = a[0]+a[1]
c = a[2]
print('Yes' if b == c else 'No')
#2022/8/12 00:01:46