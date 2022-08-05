def calc_salary(idx):
    if len(subordinate[idx]) == 0:
        return 1
    minP = 10**9
    maxP = 0
    for s in subordinate[idx]:
        P = calc_salary(s)
        minP = min(P,minP)
        maxP = max(P,maxP)
    return minP+maxP+1


N = int(input())
B = []
salary = [0 for _ in range(N+1)]
subordinate = [[] for _ in range(N+1)]
for i in range(2,N+1):
    b = int(input())
    subordinate[b].append(i)
print(calc_salary(1))