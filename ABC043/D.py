s = input()
n = len(s)

if n == 2:
    if s[0] == s[1]:
        print(1,2)
    else:
        print(-1,-1)
    exit()

cnt = 0
for i in range(n-2):
    if s[i] == s[i+1]:
        cnt += 1
    if s[i+1] == s[i+2]:
        cnt += 1
    if s[i] == s[i+2]:
        cnt += 1
    if cnt > 0:
        print(i+1,i+3)
        exit()
print(-1,-1)

#2022/8/9 00:09:41 1WA