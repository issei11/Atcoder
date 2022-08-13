sx,sy,tx,ty = map(int,input().split())
ans = []
for i in range(sy,ty):
    ans.append('U')
for i in range(sx,tx):
    ans.append('R')
for i in range(sy,ty):
    ans.append('D')
for i in range(sx,tx):
    ans.append('L')
ans.append('L')
for i in range(sy,ty+1):
    ans.append('U')
for i in range(sx,tx+1):
    ans.append('R')
ans.append('D')
ans.append('R')
for i in range(sy,ty+1):
    ans.append('D')
for i in range(sx,tx+1):
    ans.append('L')
ans.append('U')
print(*ans,sep='')
#2022/8/13 00:11:15