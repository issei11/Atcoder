N = int(input())
A = [0] + list(map(int,input().split()))

cnt = [0 for _ in range(N+1)]
for a in A:
    cnt[a] += 1

ans = 0
for i in range(1,N+1):
    ans += cnt[i]*(cnt[i]-1)//2

for i in range(1,N+1):
    tmp = ans
    tmp -= cnt[A[i]]*(cnt[A[i]]-1)//2
    tmp += max(cnt[A[i]]-2,0)*(cnt[A[i]]-1)//2
    print(tmp)
#2022/6/5 00:12:47