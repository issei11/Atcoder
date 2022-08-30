N = input()
x = 0
for i in range(len(N)):
    x += int(N[i])
print('Yes' if int(N)%x == 0 else 'No')
#2022/8/30 00:02:24