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
m = 10**9+7

comp_tmp,length_tmp = RLE(S)

check_list = ['a','t','c','o','d','e','r']
check = set(check_list)

comp = []
length = []

for i in range(len(comp_tmp)):
    if comp_tmp[i] in check:
        comp.append(comp_tmp[i])
        length.append(length_tmp[i])
print(comp,length)


#2022/9/20 00:00:00