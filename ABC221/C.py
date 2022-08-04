import itertools

N_str = input()
N = int(N_str)


#桁数
x = N
d = 0
while x > 0:
    x = x//10
    d += 1

per = N_str
per_list = list(itertools.permutations(per,d))

ans = 0
for p in per_list:
    for i in range(1,d):
        if p[i] != '0' and p[0] != '0':
            ans = max(ans,int("".join(list(p[:i])))*int("".join(list(p[i:]))))
print(ans)
#2022/5/8 00:33:30