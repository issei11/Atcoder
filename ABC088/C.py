c = [list(map(int,input().split())) for _ in range(3)]
for a1 in range(c[0][0]+1):
    b1 = c[0][0]-a1
    b2 = c[0][1]-a1
    b3 = c[0][2]-a1
    a2 = c[1][0]-b1
    a3 = c[2][0]-b1
    if c[1][1] == a2+b2 and c[2][1] == a3+b2 and c[1][2] == a2+b3 and c[2][2] == a3+b3:
        print('Yes')
        exit()
print('No')
#2022/8/31 00:09:49