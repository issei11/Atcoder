def RLE(sequence):#ランレングス圧縮
    #戻り値の初期化
    comp_seq = []
    lengths = []
    #最初の要素を記録
    comp_seq.append(sequence[0])
    tmp = sequence[0]
    length = 1
    #2板目から最後まで
    for i in range(1,len(sequence)):
        if sequence[i] != tmp:
            lengths.append(length)
            comp_seq.append(sequence[i])
            tmp = sequence[i]
            length = 1
        else:
            length += 1
    lengths.append(length)
    return comp_seq,lengths

S = input()
T = input()
c,l = RLE(S)
T_start = -1
for i in range(len(c)):
    if i > 0:
        if l[i] == len(T)-1:
            if c[i-1] == T[0]:
                T_start = i-1
    if l[i] >= len(T) and c[i] == '?':
        T_start = i
if T_start == -1:
    print('UNRESTORABLE')
    exit()
ans = []
i = 0
while i < len(c):
    if i != T_start:
        if c[i] == '?':
            for j in range(l[i]):
                ans.append('a')
        else:
            for j in range(l[i]):
                ans.append(c[i])
        i += 1
    else:
        if c[i] == '?':
            for j in range(len(T)-l[i]):
                ans.append('a')
            for j in range(len(T)):
                ans.append(T[j])
            i += 1
        else:
            for j in range(l[i]):
                ans.append(c[i])
            for j in range(1,len(T)):
                ans.append(T[j])
            i += 2
print(*ans,sep='')

#2022/8/28 00:19:10