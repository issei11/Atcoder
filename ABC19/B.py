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

s = input()
comp,l = RLE(s)
ans = []
for i in range(len(comp)):
    ans.append(comp[i])
    ans.append(l[i])
print(*ans,sep='')

#2022/8/4 00:02:51