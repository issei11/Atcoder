P = list(map(int,input().split()))
a = [chr(ord('a')+i) for i in range(26)]
ans = []
for i in P:
    ans.append(a[i-1])
print(*ans,sep='')
#2022/5/12 00:04:04