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
a = list(map(int,input().split()))

a.sort()
c,l = RLE(a)
i = 0
ans = 0
amari = sum(l)-len(l)
a = c
N = len(a)
while i < N:
    if a[i] == ans:
        amari += 1
        i += 1
    elif a[i] == ans+1:
        i += 1
        ans += 1
    elif a[i] > ans+1:
        if amari + N-i < 2:
            break
        else:
            if amari >= 2:
                amari -= 2
            else:
                N -= 2-amari
                amari = 0
            ans += 1
print(ans+amari//2)