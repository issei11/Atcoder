N = int(input())
A = set({})
for i in range(N):
    A_i = tuple(map(int,input().split()))#A_i[0] = L_i
    A.add(A_i)

print(len(A))