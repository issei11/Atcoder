n = int(input())
mod = 10007

a = [0,0,1]
for i in range(3,n):
    a.append((a[i-1]+a[i-2]+a[i-3])%mod)
print(a[n-1])
#2022/7/27 00:04:29