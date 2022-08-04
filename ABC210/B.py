N = int(input())
S = input()

i = 0
while True:
    if i%2 == 0:
        if S[i] == '1':
            print("Takahashi")
            break
    else:
        if S[i] == '1':
            print("Aoki")
            break
    i += 1
#2022/6/17 00:03:16