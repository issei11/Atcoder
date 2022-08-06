N = int(input())
num = N
cnt = 0
while num > 0:
    num = num//2
    cnt += 1

if N == 1:
    print('Aoki')
    exit()

if cnt%2 == 0:
    x = 1
    for i in range(cnt-2):
        if i%2 == 0:
            x = x*2
        else:
            x = x*2+1
    if x*2 <= N:
        print('Takahashi')
    else:
        print('Aoki')
else:
    x = 1
    for i in range(cnt-2):
        if i%2 == 0:
            x = x*2+1
        else:
            x = x*2
    if x*2 > N:
        print('Takahashi')
    else:
        print('Aoki')
#2022/8/6 00:38:51