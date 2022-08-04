N = int(input())
data = set()
for i in range(N):
    S_T = input()
    data.add(S_T)
print('Yes' if len(data) != N else 'No')
#2022/5/17 00:02:57