k,x = map(int,input().split())
left = max(-1000000,x-k+1)
right = min(1000000,x+k-1)
ans = [i for i in range(left,right+1)]
print(*ans)
#2022/7/16 00:04:39