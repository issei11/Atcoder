N,M = map(int,input().split())
if M > N*4 or M < N*2:
    print('-1 -1 -1')
    exit()
num = M-N*2
ans = [N,0,0]
if num > 0:
    if num%2 == 0:
        ans = [N-num//2,0,num//2]
    else:
        ans = [N-num//2-1,1,num//2]
print(*ans)
#2022/7/27 00:10:05