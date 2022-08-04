S,T = map(int,input().split())
cnt = 0
for a in range(S+1):
    for b in range(S+1):
        for c in range(S+1):
            if a+b+c <= S and a*b*c <= T:
                cnt += 1
print(cnt)

#2022/6/1 00:02:58