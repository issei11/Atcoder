N = int(input())
sum_table = 2025
x = sum_table-N
for i in range(1,min(x+1,10)):
    if i*(x//i) == x and x//i < 10:
        print(i,'x',x//i)
#2022/7/22 00:06:51 2WA