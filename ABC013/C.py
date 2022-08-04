N,H = map(int,input().split())
A,B,C,D,E = map(int,input().split())

ans = 0
if A*(D+E) <= C*(B+E):
    ans = A(E*N-H)/B+E

#2022/8/2 00:27:26