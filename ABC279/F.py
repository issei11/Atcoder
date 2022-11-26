N,Q = map(int,input().split())
ball = [0 for _ in range(N+Q)]
box = [i for i in range(N+1)]
cnt = N
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        ball[box[query[2]]] = 
        box[query[2]] = 0
    elif query[0] == 2:
        cnt += 1
        ball[cnt] = query[1]
    elif query[0] == 3:
        print(ball[query[1]])