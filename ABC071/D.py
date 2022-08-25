mod = 10**9+7
N = int(input())
S_1 = input()
S_2 = input()
ans = 1
if S_1[0] == S_2[0]:
    ans = (ans*3)%mod
else:
    ans = (ans*6)%mod
for i in range(1,N):
    if S_1[i] == S_1[i-1]:
        continue
    if S_1[i] == S_2[i]:
        if S_1[i-1] == S_2[i-1]:
            ans = (ans*2)%mod
    else:
        if S_1[i-1] == S_2[i-1]:
            ans = (ans*2)%mod
        else:
            ans = (ans*3)%mod
print(ans%mod)
#2022/8/25 00:14:43