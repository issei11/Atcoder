N = int(input())

l = [True]*(2*N+2)
i = 1
while True:
    if l[i]:
        print(i,flush=True)
        l[i] = False
        i += 1
    else:
        i += 1
        continue
    A = int(input())
    if not A:
        break
    l[A] = False

#2022/5/4