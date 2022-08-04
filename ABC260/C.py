def red(x,y):
    return [x+1,x*y]

def blue(x,y):
    return [1,y]

N,X,Y = map(int,input().split())

r1 = 1
r2 = 0
b1 = 0
b2 = 0

while N > 1:
    r2 = r1*(X+1) + b1
    b2 = r1*X*Y + b1*Y
    r1 = r2
    b1 = b2
    N -= 1
print(b1)
