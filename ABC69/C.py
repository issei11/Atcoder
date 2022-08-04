N =int(input())
a = list(map(int,input().split()))

num4 = 0
num2 = 0
for i in range(N):
    if a[i]%2 == 0:
        num2 += 1
        if a[i]%4 == 0:
            num4 += 1

if num4 >= N//2:
    print('Yes')
else:
    if N-num4*2 <= num2-num4:
        print('Yes')
    else:
        print('No')
#2022/7/21 00:13:16