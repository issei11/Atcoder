N = int(input())
a,b = map(int,input().split())
K = int(input())
l = [a,b]
P = l+list(map(int,input().split()))
s = set(P)
print('YES' if len(P) == len(s) else 'NO')
#2022/8/4 00:04:21