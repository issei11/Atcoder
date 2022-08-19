O = input()
E = input()
ans = []
for i in range(len(E)):
    ans.append(O[i])
    ans.append(E[i])
if len(O) > len(E):
    ans.append(O[len(O)-1])
print(*ans,sep='')
#2022/8/17 00:02:30