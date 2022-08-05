import math
N = int(input())
R = []
for _ in range(N):
    R.append(int(input()))
R = sorted(R,reverse=True)
ans = 0
for i in range(N):
    if i%2 == 0:
        ans += R[i]**2
    else:
        ans -= R[i]**2
print(ans*math.pi)
#2022/8/5 00:04:43