N,K = input().split()
K = int(K)
N = int(N)
D = list(map(int,input().split()))
like = []
for i in range(10):
    if i not in D:
        like.append(i)

l = len(like)

ans = ['0','0','0','0','0']
if N <= 10:
    for i5 in range(l):
        ans[4] = str(like[i5])
        if N <= int(''.join(ans)):
            print(int(''.join(ans)))
            exit()
    if like[0] == 0:
        ans[3] = str(like[1])
    else:
        ans[3] = str(like[0])
    ans[4] = str(like[0])
    print(int(''.join(ans)))

elif N<=100:
    for i4 in range(l):
        for i5 in range(l):
            ans[3] = str(like[i4])
            ans[4] = str(like[i5])
            if N <= int(''.join(ans)):
                print(int(''.join(ans)))
                exit()

    if like[0] == 0:
        ans[2] = str(like[1])
    else:
        ans[2] = str(like[0])
    ans[3] = str(like[0])
    ans[4] = str(like[0])
    print(int(''.join(ans)))

elif N<=1000:
    for i3 in range(l):
        for i4 in range(l):
            for i5 in range(l):
                ans[2] = str(like[i3])
                ans[3] = str(like[i4])
                ans[4] = str(like[i5])
                if N <= int(''.join(ans)):
                    print(int(''.join(ans)))
                    exit()

    if like[0] == 0:
        ans[1] = str(like[1])
    else:
        ans[1] = str(like[0])
    ans[2] = str(like[0])
    ans[3] = str(like[0])
    ans[4] = str(like[0])
    print(int(''.join(ans)))

elif N<=10000:
    for i2 in range(l):
        for i3 in range(l):
            for i4 in range(l):
                for i5 in range(l):
                    ans[1] = str(like[i2])
                    ans[2] = str(like[i3])
                    ans[3] = str(like[i4])
                    ans[4] = str(like[i5])
                    if N <= int(''.join(ans)):
                        print(int(''.join(ans)))
                        exit()

    if like[0] == 0:
        ans[0] = str(like[1])
    else:
        ans[0] = str(like[0])
    ans[1] = str(like[0])
    ans[2] = str(like[0])
    ans[3] = str(like[0])
    ans[4] = str(like[0])
    print(int(''.join(ans)))
#2022/8/9 00:45:19 4WA