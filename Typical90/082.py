L,R = map(int,input().split())
mod = 10**9+7

digit_L = len(str(L))
digit_R = len(str(R))
if digit_L == digit_R:
    print((digit_R*(R-L+1)*(R+L)//2)%mod)
else:
    ans = 0
    r = 0
    l = 0
    for d in range(digit_L,digit_R+1):
        r = 10**d-1
        l = 10**(d-1)
        if d == digit_L:
            l = L
        if d == digit_R:
            r = R
        ans += (d*(r-l+1)*(r+l)//2)%mod
    print(ans%mod)
#2022/9/19 00:10:41