N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = [0]+A
B = [0]+B

cnt1 = 0
cnt2 = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        if A[i] == B[j]:
            if i == j:
                cnt1 += 1
            else:
                cnt2 += 1

print(cnt1)
print(cnt2)

#2022/4/21 00:05:22