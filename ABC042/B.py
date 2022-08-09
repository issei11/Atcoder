N,L = map(int,input().split())
S = [input() for _ in range(N)]

S.sort()
print(*S,sep='')
#2022/8/9 00:02:37