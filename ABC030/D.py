N,a_input = map(int,input().split())
k = input()
b = list(map(int,input().split()))
b = list(map(lambda x: x-1,b))
a = a_input-1


s = set()
s.add(a)
step = 0
while True:
    a = b[a]
    step += 1
    if a in s:
        break
    s.add(a)
s = set()
s.add(a)
cycle = 0
while True:
    a = b[a]
    cycle += 1
    if a in s:
        break
    s.add(a)
if len(k) < 20:
    k = int(k)
    if k <= step-cycle:
        a = a_input-1
        for i in range(k):
            a = b[a]
        print(a+1)
        exit()
    k = k-(step-cycle)
    k = k%cycle
    for i in range(k):
        a = b[a]
    print(a+1)


#2022/8/6