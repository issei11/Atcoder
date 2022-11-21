H,M = map(int,input().split())
A = H//10
B = H%10
C = M//10
D = M%10

while(True):
    h = 10*A + C
    m = 10*B + D
    if 0 <= h <=23 and 0 <= m <= 59:
        break
    else:
        D += 1
        if D == 10:
            D = 0
            C += 1
            if C == 6:
                C = 0
                B += 1
                if B == 10:
                    B = 0
                    A += 1
                if 10*A+B >= 24:
                    A = 0
                    B = 0

print(10*A+B,10*C+D)