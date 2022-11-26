def f(A,B):
    return (A/(2*B))**(2/3)-1
def g(A,B,n):
    return A/((n+1)**0.5)+B*n

A,B = map(int,input().split())
n = 0
x = f(A,B)
if x <= 0:
    print(A)
else:
    print('{:.8f}'.format(min(g(A,B,int(x)),g(A,B,int(x)+1))))