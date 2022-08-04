N = int(input())

M = N*2
print(M)

x = []
if N%4 > 0:
    x.append(N%4)
    N -= N%4
while N > 0:
    N -= 4
    x.append(4)

print(*x, sep= '')