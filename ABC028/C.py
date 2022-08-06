A = list(map(int,input().split()))
ans = []
for i in range(len(A)):
    for j in range(i+1,len(A)):
        for k in range(j+1,len(A)):
            ans.append(A[i]+A[j]+A[k])
ans.sort()
print(ans[-3])
#2022/8/6 00:02:39