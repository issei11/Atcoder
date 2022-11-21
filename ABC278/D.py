N = int(input())
A = list(map(int,input().split()))
Q = int(input())

all = -1
all_count = 0
check = [0 for i in range(N)]
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        all = query[1]
        all_count += 1
    if query[0] == 2:
        if all_count == check[query[1]-1]:
            A[query[1]-1] += query[2]
        else:
            check[query[1]-1] = all_count
            A[query[1]-1] = all + query[2]
    if query[0] == 3:
        if all_count == check[query[1]-1]:
            print(A[query[1]-1])
        else:
            print(all)


