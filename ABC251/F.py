import random
def partition(A, cur_node, end):
    pivot = A[end]
    i = cur_node - 1
    for j in range(cur_node, end):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i] 
    A[i+1], A[end] = A[end], A[i+1]
    print(A)
    return i+1
        
def quicksort(A, cur_node, end):
    if cur_node < end:
        pivot_position = partition(A, cur_node, end)
        quicksort(A, cur_node, pivot_position -1)
        quicksort(A,pivot_position + 1, end)
    
        
A = list(range(1,11))
random.shuffle(A)
print(A)
quicksort(A, 0, len(A)-1)
print(A)