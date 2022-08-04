a = int(input())
b = int(input())
A = a
B = b
i = 0
while A%10 != B%10:
    A -= 1
    i += 1
A = a
B = b
j = 0
while A%10 != B%10:
    A += 1
    j += 1

print(min(i,j))
#2022/8/2 00:03:22