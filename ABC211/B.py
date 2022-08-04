S = []

S1 = input()
S2 = input()
S3 = input()
S4 = input()

S.append(S1)
S.append(S2)
S.append(S3)
S.append(S4)

S = set(S)

print("Yes" if S == {"H","2B","3B","HR"} else "No")
#2022/6/18 00:03:01