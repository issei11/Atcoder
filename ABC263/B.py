N = int(input())
P = [0] + [0] + list(map(int,input().split()))
cnt = 0
while True:
    N = P[N]
    cnt += 1
    if N == 1:
        print(cnt)
        break