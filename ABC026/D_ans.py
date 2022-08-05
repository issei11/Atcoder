import math
def f(t):
    return A*t+B*math.sin(C*t*math.pi)

A,B,C = map(int,input().split())
t_left = 0
t_right = 200
f_left = f(t_left)
f_right = f(t_right)
if abs(f_left-100) < 10**(-7):
    print(t_left)
    exit()
if abs(f_right-100) < 10**(-7):
    print(t_right)
    exit()
while True:
    t_pivot = (t_left+t_right)/2
    f_pivot = f(t_pivot)
    if abs(f_pivot-100) < 10**(-7):
        print(t_pivot)
        break
    elif f_pivot < 100:
        t_left = t_pivot
    else:
        t_right = t_pivot