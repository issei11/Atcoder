N = int(input())
word = set()
W1 = input()
word.add(W1)
flag = True
for i in range(1,N):
    W2 = input()
    if W1[-1] != W2[0] or W2 in word:
        flag = False
    W1 = W2
    word.add(W2)
print("Yes" if flag else "No")
#2022/6/15 00:08:05