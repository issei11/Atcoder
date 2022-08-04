A = int(input())
B = int(input())
C = int(input())


S = sorted([A,B,C],reverse=True)
T = [A,B,C]
for i in range(3):
    for j in range(3):
        if S[j] == T[i]:
            print(j+1)
            break