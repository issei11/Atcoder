S = input()

S_all = [S]
for i in range(1,len(S)):
    S_all.append(S[i:]+S[:i])

S_all = sorted(S_all)
print(S_all[0])
print(S_all[-1])
#2022/5/7 00:11:40