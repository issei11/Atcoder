S = input()
n = len(S)
if n == 1:
    print(''.join([S+S+S+S+S+S]))
elif n == 2:
    print(''.join([S+S+S]))
else:
    print(''.join([S+S]))