N,A,B = map(int,input().split())
if A <= B:
    ans = 0
    if N >= A:
        ans = N-A+1
    print(ans)
else:
    ans = 0
    if N >= A:
        cycle = (N-A+1)//A
        ans += B*cycle
        ans += min(N-A+1-cycle*A,B)
    print(ans)