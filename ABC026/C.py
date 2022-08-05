def calc_salary(idx):
    if len(subordinate[idx]) == 0:
        return 1
    calc = []
    for i in range(len(subordinate[idx])):
        if salary[subordinate[idx][i]] == 0:
            salary[subordinate[idx][i]] = calc_salary(subordinate[idx][i])
            calc.append(salary[subordinate[idx][i]])
        else:
            calc.append(salary[subordinate[idx][i]])
    return min(calc)+max(calc)+1


N = int(input())
B = []
salary = [0 for _ in range(N+1)]
subordinate = [[] for _ in range(N+1)]
for i in range(2,N+1):
    b = int(input())
    subordinate[b].append(i)
print(calc_salary(1))

#2022/8/5 00:21:17