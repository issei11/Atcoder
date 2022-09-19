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

N = int(input())
S = input()
R = RLE(S)
ans = N*(N-1)//2
for i in R[1]:
    if i >= 2:
        ans -= i*(i-1)//2
print(ans)



#2022/9/19 00:10:14