H,W = map(int,input().split())
G = [input() for _ in range(H)]
done = [[False for _ in range(W)]for _ in range(H)]
i = 0
j = 0
done[i][j] = True
while True:
    if G[i][j] == 'U' and i != 0:
        i -= 1
        if done[i][j] == True:
            print(-1)
            exit()
        done[i][j] = True
        continue
    elif G[i][j] == 'D' and i != H-1:
        i += 1
        if done[i][j] == True:
            print(-1)
            exit()
        done[i][j] = True
        continue
    elif G[i][j] == 'L' and j != 0:
        j -= 1
        if done[i][j] == True:
            print(-1)
            exit()
        done[i][j] = True
        continue
    elif G[i][j] == 'R' and j != W-1:
        j += 1
        if done[i][j] == True:
            print(-1)
            exit()
        done[i][j] = True
        continue
    else:
        print(i+1,j+1)
        exit()