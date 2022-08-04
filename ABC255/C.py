X,A,D,N = map(int,input().split())
if D >= 0:
    if X-A <= 0:
        print(A-X)
    elif A+(N-1)*D <= X:
        print(X-(A+(N-1)*D))
    else:
        K = (X-A)//D
        print(min(X-(A+K*D),(A+(K+1)*D)-X))
else:
    if X >= A:
        print(X-A)
    elif A+(N-1)*D >= X:
        print((A+(N-1)*D)-X)
    else:
        K = (X-A)//D
        print(min(abs(X-(A+K*D)),abs((A+(K+1)*D)-X)))