N = int(input())
town = []
s = 0
for _ in range(N):
    S,P = input().split()
    P = int(P)
    town.append([S,P])
    s += P
for i in range(N):
    if 2*town[i][1] > s:
        print(town[i][0])
        exit()
print('atcoder')
#2022/8/8 00:04:19