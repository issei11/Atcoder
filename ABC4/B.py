C = []
for _ in range(4):
    c = list(input().split())
    C.append(c)
for i in range(1,5):
    C[-i].reverse()
    print(*C[-i])
    #2022/7/22 00:06:10