N = int(input())
X = [0] + list(map(int,input().split()))
C = [0] + list(map(int,input().split()))

#0未発見 1発見済みだが閉路に関係ない 2閉路に関係あり
check = [0 for _ in range(N+1)]

ans = 0

c = []

i = 1
start = 0
now = 0
while i < N+1:
    if check[i] == 0:
        check[i] = 1
        start = i
    else:
        i += 1
        continue
    now = start
    while True:
        if check[X[now]] == 0:
            c.append(C[now])
            now = X[now]
            check[now] = 1
        elif check[X[now]] == 1:
            break
        elif check[X[now]] == 2:
            c = []
            break