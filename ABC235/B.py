N = int(input())
H = list(map(int,input().split()))

tmp = 0

while H[tmp] < H[tmp+1]:
    tmp += 1
    if tmp == N-1:
        break

print(H[tmp])
#2022/4/28 00:07:03