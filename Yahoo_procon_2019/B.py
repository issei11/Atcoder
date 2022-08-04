A = []
a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
a3,b3 = map(int,input().split())

A.append(a1)
A.append(a2)
A.append(a3)
A.append(b1)
A.append(b2)
A.append(b3)

B = [0,0,0,0]

for i in range(6):
    B[A[i]-1] += 1

B.sort()
if B == [1,1,2,2]:
    print("YES")
else:
    print("NO")
#2022/6/15 00:05:45