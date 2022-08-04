N = int(input())
ans = []
while N > 0:
    if N%2 == 0:
        N = N//2
        ans.append('B')
    else:
        N -= 1
        ans.append('A')
ans.reverse()
print(''.join(ans))
#2022/5/17 00:05:51