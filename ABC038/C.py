import math
def combinations_count(n, r):#組み合わせの計算, import math を忘れずに
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
a = list(map(int,input().split()))
cnt = 0
ans = N
for i in range(N-1):
    if a[i] < a[i+1]:
        cnt += 1
    else:
        if cnt > 0:
            ans += combinations_count(cnt+1,2)
        cnt = 0
if cnt > 0:
    ans += combinations_count(cnt+1,2)
print(ans)