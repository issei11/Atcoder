N = int(input())
A = list(map(int,input().split()))

A.sort()
a = A[-1]
b = A[-2]
c = A[-3]

ans = [str(a),str(b),str(c)]
ans = sorted(ans, reverse=True)
print(*ans,sep='')