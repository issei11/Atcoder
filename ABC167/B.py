A,B,C,K = map(int,input().split())
if K <= A:
    print(K)
elif K <= A+B:
    print(A)
else:
    print(A-(K-(A+B)))
#2022/7/15 00:02:45