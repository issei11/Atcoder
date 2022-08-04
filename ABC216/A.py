x_y = float(input())
x = int(x_y)
y = int((x_y-x)*10)
if 0 <= y < 3:
    print(f'{x}-')
elif 3 <= y < 7:
    print(x)
else:
    print(f'{x}+')
#2022/5/16 00:03:49