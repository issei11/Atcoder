w = input()
d = dict()
for i in range(len(w)):
    if w[i] in d:
        d[w[i]] += 1
    else:
        d[w[i]] = 1
for key in d.keys():
    if d[key]%2 != 0:
        print('No')
        exit()
print('Yes')
#2022/8/11 00:04:48