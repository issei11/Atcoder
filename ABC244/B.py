N = int(input())
T = input()

x, y = 0, 0

vec = 0
for i in range(N):
    if T[i] == 'S':
        if vec%4 == 0:
            x += 1
        elif vec%4 == 1:
            y -= 1
        elif vec%4 == 2:
            x -= 1
        elif vec%4 == 3:
            y += 1
    if T[i] == 'R':
        vec += 1

print(f"{x} {y}")

#2022/4/20 00:09:15