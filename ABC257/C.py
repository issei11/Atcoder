N = int(input())
S = input()
W = list(map(int,input().split()))
adult = []
child = []
for i in range(N):
    if S[i] == '0':
        child.append(W[i])
    else:
        adult.append(W[i])

adult.sort()
child.sort()
adult_num = len(adult)
child_num = len(child)

i = 0
j = 0
ans = 0
tmp = 0
while True:
    tmp = adult_num-i + j
    ans = max(tmp,ans)
    if i == adult_num and j == child_num:
        break
    elif i == adult_num:
        j += 1
    elif j == child_num:
        i += 1
    else:
        if adult[i] < child[j]:
            i += 1
        elif adult[i] > child[j]:
            j += 1
        else:
            i += 1
            j += 1
print(ans)
