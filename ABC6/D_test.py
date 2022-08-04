from bisect import bisect_left

def get_lis(A):
  smallest = [10**18] * len(A)
  for i in range(N):
    idx = bisect_left(smallest, A[i])
    smallest[idx] = min(A[i], smallest[idx])

  return max(i+1 for i in range(N) if smallest[i] < 10**18)

N = int(input())
A = []
for i in range(N):
  A.append(int(input()))

lis = get_lis(A)
print(N-lis)