N = int(input())

A0 = [1]
A1 = [1,1]
print(*A0)
if N > 1:
    print(*A1)
A2 = [1]

for i in range(2,N):
    for j in range(1,i):
        A2.append(A1[j]+A1[j-1])
    A2.append(1)
    print(*A2)
    A1 = A2
    A2 = [1]