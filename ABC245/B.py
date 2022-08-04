N =int(input())
A = list(map(int, input().split()))

frag = True
ans = 0
while frag:
    for l in A:
        if l == ans:
            ans += 1
            break
    else:
        frag = False

print(ans)

#2022/4/19 00:07:22