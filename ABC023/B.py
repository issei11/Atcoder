N = int(input())
S = input()

if N%2 == 0:
    print(-1)
    exit()
else:
    N = N//2

for i in range(N+1):
    if i%3 == 0:
        if not(S[N-i] == 'b' and S[N+i] == 'b'):
            print(-1)
            exit()
    elif i%3 == 1:
        if not(S[N-i] == 'a' and S[N+i] == 'c'):
            print(-1)
            exit()
    else:
        if not(S[N-i] == 'c' and S[N+i] == 'a'):
            print(-1)
            exit()
print(N)
#2022/8/5 00:10:00