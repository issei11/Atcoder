import math
def f(t):
    return A*t+B*math.sin(C*t*math.pi)

A,B,C = map(int,input().split())
if 2*B*C <= A:
    t_left = 0
    t_right = 100
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
else:
    m = 0
    f_left = 0
    f_right = 2*B*C+A
    while True:
        if m%4 == 0:
            if f_left <= 2*C*100 and 2*C*100 <= f_right:
                break
            m += 2
            f_left = f_right
            f_right = A*(m+1)-2*B*C
        else:
            if f_left >= 2*C*100 and 2*C*100 >= f_right:
                break
            m += 2
            f_left = f_right
            f_right = A*(m+1)+2*B*C
    t_left = (m-1)/(2*C)
    t_right = (m+1)/(2*C)
    if abs(f_left-2*C*100) < 10**(-7):
        print(t_left)
        exit()
    if abs(f_right-2*C*100) < 10**(-7):
        print(t_right)
        exit()
    if m%4 == 0: # 単調増加
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
    else: #単調減少
        while True:
            t_pivot = (t_left+t_right)/2
            f_pivot = f(t_pivot)
            if abs(f_pivot-100) < 10**(-7):
                print(t_pivot)
                break
            elif f_pivot > 100:
                t_left = t_pivot
            else:
                t_right = t_pivot
#2022/8/5 01:08:01