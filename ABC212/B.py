X = input()

X = [int(i) for i in X]

flug = True
if len(set(X)) == 1:
    flug = False
Y = []
for i in range(4):
    Y.append((X[i]+(3-i))%10)
if len(set(Y)) == 1:
    flug = False
print("Strong" if flug else "Weak")
#2022/6/3 00:09:40