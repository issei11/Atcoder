N,K = map(int,input().split())
A = [0] + list(map(int,input().split()))
B = [0] + list(map(int,input().split()))
check = []
for i in B:
    check.append(A[i])
print('Yes' if max(A) == max(check) else 'No')
#2022/5/31 00:07:16