s = input()
k = int(input())
if k > len(s):
    print(0)
    exit()
ans = set()
ans.add(s[:k])
for i in range(1,len(s)-k+1):
    if s[i:i+k] not in ans:
        ans.add(s[i:i+k])
print(len(ans))
#2022/8/8 00:06:43 1WA