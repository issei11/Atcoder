a,b,k = map(int,input().split())

num = a
cnt = 0

while num < b:
    num = num*k
    cnt += 1

print(cnt)

#2022/4/19 00:04:28