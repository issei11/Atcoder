a,b,c,d = map(int, input().split())

if a < c:
    print("Takahashi")
elif a == c:
    if b <= d:
        print("Takahashi")
    else:
        print("Aoki")
else:
    print("Aoki")

#2022/4/19 00:03:50