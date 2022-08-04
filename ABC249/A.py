a,b,c,d,e,f,x = map(int, input().split())

sum_T = 0
sum_A = 0

for i in range(x):
    if i%(a+c) < a:
        sum_T += b
    if a+c > i%(a+c) > a:
        sum_T += 0

for i in range(x):
    if i%(d+f) < d:
        sum_A += e
    if d+f > i%(d+f) > d:
        sum_A += 0

if sum_A > sum_T:
    print('Aoki')
elif sum_A < sum_T:
    print('Takahashi')
else:
    print('Draw')