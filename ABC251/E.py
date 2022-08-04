def qsort(seq,left,right):
    if left >= right:
        return
    pivot = seq[(left+right)//2]
    cur_l = left
    cur_r = right
    while True:
        if seq[cur_l] < pivot:
            cur_l += 1
            if cur_l == right:
                break
        if seq[cur_r] >= pivot:
            cur_r -= 1
            if cur_r == left:
                break
        if cur_r <= cur_l:
            break
        elif seq[cur_l] >= pivot >= seq[cur_r]:
            seq[cur_l],seq[cur_r] = seq[cur_r],seq[cur_l]
            print('swapped')
        print(seq,left,right,cur_l,cur_r)
    qsort(seq,left,cur_l)
    qsort(seq,cur_l+1,right)

N = int(input())
A = list(map(int,input().split()))
qsort(A,0,len(A)-1)
print(*A)