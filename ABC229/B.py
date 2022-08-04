A,B = input().split()
frag = 1
for i in range(1,min([len(A),len(B)])+1):
    tmp = int(A[-i])+int(B[-i])
    if tmp >= 10:
        print('Hard')
        frag = 0
        break
if frag:
    print('Easy')
#2022/5/3 00:05:57