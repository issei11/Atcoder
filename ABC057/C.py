def f(a,b):
    a = str(a)
    b = str(b)
    return(max(len(a),len(b)))

N = int(input())
ans = float('inf')
i = 1
while i*i <= N:
    j = N//i
    if j*i != N:
        i += 1
        continue
    tmp = f(i,j)
    ans = min(tmp,ans)
    i += 1
print(ans)
#2022/8/17 00:05:29