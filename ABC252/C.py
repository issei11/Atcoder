N = int(input())
t = 0
S = []
for i in range(N):
    S.append(input())

for num in range(10):








check = [0 for i in range(10)] #0-9
for i in range(N):
    S = input()
    for j in range(10):
        s = int(S[j])
        if check[s] < j:
            check[s] = j
print(min(check))

#解けなかった。