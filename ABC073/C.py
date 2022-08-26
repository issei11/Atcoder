N = int(input())
paper = set()
for _ in range(N):
    a = int(input())
    if a in paper:
        paper.discard(a)
    else:
        paper.add(a)
print(len(paper))
#2022/8/26 00:02:56