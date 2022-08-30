A,B = map(int,input().split())
S = input()
i = 0
while i < A:
    if S[i] == '-':
        print('No')
        exit()
    i += 1
if S[i] != '-':
    print('No')
    exit()
i += 1
while i < A+B+1:
    if S[i] == '-':
        print('No')
        exit()
    i += 1
print('Yes')
#2022/8/30 00:04:07