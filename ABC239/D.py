def prime(N):
    list = []
    for number1 in range(2,N+1):
        count=0
        for number2 in range(1,number1):
                number=number1%number2
                if number==0:
                    count+=1
        if count==1:
            list.append(number1)
    return list

A,B,C,D = map(int,input().split())
prime = prime(B+D)

cnt = 0
win = 'Aoki'

for i in range(A,B+1):
    for j in range(C,D+1):
        if i+j in prime:
            break
        else:
            cnt += 1
    if cnt == D+1-C:
        win = 'Takahashi'
    cnt = 0

print(win)

#2022/4/25 00:17:06