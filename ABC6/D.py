N = int(input())
check = [0 for _ in range(N+2)]
back = 0
for _ in range(N):
    c = int(input())
    if check[c+1] == 1:
        back += 1
        check[c] = 1
    else:
        check[c] = 1
print(back)

#2022/7/29