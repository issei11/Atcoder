N = int(input())

num = []
r = 0
while N > 0:
    r = N%26
    if 0 < r:
        num.append(r)
        N //= 26
    else:
        num.append(r+26)
        N = N//26 - 1

name = []
for i in range(1,len(num)+1):
    name.append(chr(num[-i]+96))
print("".join(name))
#2022/6/6 00:27:45