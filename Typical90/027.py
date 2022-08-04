N = int(input())
S_set = set()
for i in range(N):
    S = input()
    if S not in S_set:
        S_set.add(S)
        print(i+1)