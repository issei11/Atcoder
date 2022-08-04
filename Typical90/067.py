def base10int(value,base):#10進法→N進法
    if value//base:
        return base10int(value//base,base)+str(value%base)
    return str(value%base)

N,K = input().split()
N = int(N,8)#10進法に変換
K = int(K)
for i in range(K):
    N = base10int(N,9)
    tmp = N.replace('8','5')
    N = int(tmp,8)
print(int(base10int(N,8)))