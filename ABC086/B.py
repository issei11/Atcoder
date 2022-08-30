a,b = input().split()
s = int(a+b)
for i in range(2000):
    if i*i == s:
        print('Yes')
        exit()
print('No')
#2022/8/30 00:02:17