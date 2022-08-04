N = int(input())

if N < 10:
    print('AGC00{}'.format(N))
else:
    print('AGC0{}'.format(N) if N < 42 else 'AGC0{}'.format(N+1))

#2022/5/3