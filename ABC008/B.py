N = int(input())
vote = dict()
for _ in range(N):
    S = input()
    if S in vote:
        vote[S] += 1
    else:
        vote[S] = 1
print(max(vote,key=vote.get))
#2022/7/30 00:05:17