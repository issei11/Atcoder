N = int(input())
S = input()

A = [N]
B = []

for i in range(1,N+1):
    if S[-i] == 'R':
        B.append(N-i)
    else:
        A.append(N-i)

B.reverse()
A = B + A
print(*A)

#2022/4/26 00:23:23