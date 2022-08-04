W = input()
ans = []
for i in range(len(W)):
    if W[i] != 'a' and W[i] != 'i' and W[i] != 'u' and W[i] != 'e' and W[i] != 'o':
        ans.append(W[i])
print(*ans,sep='')
#2022/7/21 00:03:39