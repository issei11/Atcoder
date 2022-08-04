N,K,A = map(int,input().split())

print((A+K-1)%N if (A+K-1)%N != 0 else N)
#2022/5/4 0:07:03