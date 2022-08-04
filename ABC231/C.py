def binary_search(seq,key):
    left = 0
    right = len(seq)-1

    if seq[right] < key:
        return right+1
    elif seq[left] > key:
        return left

    while left < right-1:
        pivot = (left+right)//2
        if seq[pivot] < key:
            left = pivot
        else:
            right = pivot
    return right

N,Q = map(int,input().split())
A = list(map(int,input().split()))

A_s = sorted(A)

for i in range(Q):
    x = int(input())
    n = binary_search(A_s,x)
    print(N-n)

#2022/5/2 00:58:47