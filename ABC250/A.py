H,W = map(int,input().split())
R,C = map(int,input().split())

if H == 1 and W == 1:
    print(0)
elif (H == 1 and (C == 1 or C == W)) or (W == 1 and (R == 1 or R == H)):
    print(1)
elif ((R == 1 or R == H) and (C == 1 or C == W)) or (H == 1 or W == 1):
    print(2)
elif (R != 1 and R != H) and (C != 1 and C != W):
    print(4)
else:
    print(3)