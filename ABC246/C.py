n,k,x = map(int,input().split())
a_1 = list(map(int,input().split()))
a = [0]+a_1

i = 1

while i < n+1:
    if a[i] >= x:
        k = k-a[i]//x
        a[i] = a[i]%x
    i += 1

min = 0
for i in range(1, n+1):
    min += a[i]

if k < 0:
    min += x*(-k)

def merge(left, right):
    merged = []
    l_i, r_i = 0, 0
    while l_i < len(left) and r_i < len(right):
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


data = merge_sort(a)

i = 0

while i < n and k > 0:
    min -= data[n-i]
    i += 1
    k -= 1

print(min)

#2022/4/19 02:16:43
