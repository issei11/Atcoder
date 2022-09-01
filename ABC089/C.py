N = int(input())
d = dict()
c = {'M','A','R','C','H'}
for _ in range(N):
    s = input()[0]
    if s in c:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
