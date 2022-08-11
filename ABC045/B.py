A = input()
B = input()
C = input()

a = 0
b = 0
c = 0
now = 'a'
while True:
    if now == 'a':
        if a == len(A):
            print('A')
            break
        now = A[a]
        a += 1
    elif now == 'b':
        if b == len(B):
            print('B')
            break
        now = B[b]
        b += 1
    elif now == 'c':
        if c == len(C):
            print('C')
            break
        now = C[c]
        c += 1
#2022/8/11 00:07:18