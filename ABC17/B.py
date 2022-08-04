X = input()
if len(X) == 0:
    print('YES')
    exit()
i = 0
while i < len(X):
    if X[i] == 'c' and X[i+1] == 'h':
        i += 2
    elif X[i] == 'o' or X[i] == 'k' or X[i] == 'u':
        i += 1
    else:
        print('NO')
        exit()
print('YES')
#2022/8/3 00:05:17