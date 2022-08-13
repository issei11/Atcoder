R,C = map(int,input().split())
if R == 1 or R == 15:
    print('black')
    exit()
elif R == 2 or R == 14:
    if 1 < C < 15:
        print('white')
    else:
        print('black')
    exit()
elif R == 3 or R == 13:
    if C == 2 or C == 14:
        print('white')
    else:
        print('black')
    exit()
elif R == 4 or R == 12:
    if 3 < C < 13 or C == 2 or C == 14:
        print('white')
    else:
        print('black')
    exit()
elif R == 5 or R == 11:
    if C == 4 or C == 12 or C == 2 or C == 14:
        print('white')
    else:
        print('black')
    exit()
elif R == 6 or R == 10:
    if 5 < C < 11 or C == 4 or C == 12 or C == 2 or C == 14:
        print('white')
    else:
        print('black')
    exit()
elif R == 7 or R == 9:
    if C == 6 or C == 10 or C == 4 or C == 12 or C == 2 or C == 14:
        print('white')
    else:
        print('black')
    exit()
else:
    if C%2 == 0:
        print('white')
    else:
        print('black')
    exit()