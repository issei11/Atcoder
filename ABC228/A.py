S,T,X = map(int,input().split())

if S < T:
    print('Yes' if S<=X<T else 'No')
else:
    print('Yes' if X>=S or T>X else 'No')
#2022/5/4 0:03:37