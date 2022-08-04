N,K = map(int,input().split())
R = list(map(int,input().split()))
rate = 0
R = sorted(R)
for i in range(N-K,N):
    rate += (2**(i-(N-K)))*R[i]
rate = rate/(2**K)
print(rate)
#2022/7/22 00:09:26