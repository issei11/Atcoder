import math

def combinations_count(n, r):#組み合わせの計算, import math を忘れずに
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def RLE_for(sequence):#ランレングス圧縮
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

c,l = RLE_for(S)
ans = 0
for i in range(len(l)):
    if l[i] > 1:
        ans += combinations_count(l[i],2)
print(ans)

#2022/7/18 00:16:20