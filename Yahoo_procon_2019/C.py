K,A,B = map(int,input().split())
ans = 0
if A+2 < B:
    if K >= A+1:
        K = K-(A+1)
        ans = B
        if K  == 0:
            print(ans)
        elif K == 1:
            print(ans+1)
        else:
            ans += (B-A)*(K//2)+(K%2)
            print(ans)
    else:
        print(K+1)
else:
    print(K+1)
#2022/6/14 00:16:40