S = ['a','b','c']

def f(n,s):
    if n == 0:
        print(s)
        return
    for i in range(3):
        f(n-1,s+S[i])

N = int(input())
f(N,'')