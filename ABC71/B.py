alphabet = 'abcdefghijklmnopqrstuvwxyz'
S = input()
s = set(S)
flag = True
for i in range(26):
    if not alphabet[i] in s:
        print(alphabet[i])
        flag = False
        break
if flag:
    print('None')
#2022/7/15 00:06:28