N = int(input())
A = list(map(int,input().split()))
Q = int(input())

A_cnt = [[i,0] for i in range(10**5+9)]
A_sum = sum(A)
for a in A:
    A_cnt[a][1] += 1

for i in range(Q):
    B,C = map(int,input().split())
    A_sum += (C-B)*A_cnt[B][1]
    print(A_sum)
    A_cnt[C][1] += A_cnt[B][1]
    A_cnt[B][1] = 0

#2022/6/3 00:16:48