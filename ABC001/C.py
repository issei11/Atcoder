deg,dis = map(int,input().split())
dir = []
if 562.5 <= deg < 1237.5:
    dir.append('E')
    if deg < 787.5:
        dir.append('NE')
    elif deg >= 1012.5:
        dir.append('SE')
elif 1237.5 <= deg < 2362.5:
    dir.append('S')
    if deg < 1687.5:
        if deg >= 1462.5:
            dir.append('S')
        dir.append('E')
    elif deg >= 1912.5:
        if deg < 2137.5:
            dir.append('S')
        dir.append('W')
elif 2362.5 <= deg < 3037.5:
    dir.append('W')
    if deg < 2587.5:
        dir.append('SW')
    elif deg >= 2812.5:
        dir.append('NW')
else:
    dir.append('N')
    if 3037.5 <= deg < 3487.5:
        if deg >= 3262.5:
            dir.append('N')
        dir.append('W')
    elif 112.5 <= deg < 562.5:
        if deg < 337.5:
            dir.append('N')
        dir.append('E')

W = 0
if dis < 15:
    W = 0
elif dis < 93:
    W = 1
elif dis < 201:
    W = 2
elif dis < 327:
    W = 3
elif dis < 477:
    W = 4
elif dis < 645:
    W = 5
elif dis < 831:
    W = 6
elif dis < 1029:
    W = 7
elif dis < 1245:
    W = 8
elif dis < 1467:
    W = 9
elif dis < 1707:
    W = 10
elif dis < 1959:
    W = 11
else:
    W = 12


if W == 0:
    print('C',W)
else:
    print(''.join(dir),W)

#2022/7/21 00:27:49 1WA
