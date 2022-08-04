def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

N = int(input())
A = sorted(list(map(int,input().split())))
a =max(A)


cnt_l = [0]*(2*10**5)

for i in A:
    cnt_l[i] += 1

cnt = 0

for i in range(1,a+1):
    div = make_divisors(i)
    if len(div)%2 == 0:
        for k in range(len(div)//2):
            cnt += cnt_l[div[k]]*cnt_l[div[len(div)-1-k]]
    else:
        for k in range(len(div)//2):
            cnt += cnt_l[div[k]]*cnt_l[div[len(div)-1-k]]
        cnt += cnt_l[len(div)//2]**2

print(cnt)
