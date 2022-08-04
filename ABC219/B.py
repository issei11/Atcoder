S1 = input()
S2 = input()
S3 = input()
T = input()
ans = []
for i in T:
    if i == '1':
        ans.append(S1)
    elif i == '2':
        ans.append(S2)
    elif i == '3':
        ans.append(S3)
print(''.join(ans))
#2022/5/10 00:02:44