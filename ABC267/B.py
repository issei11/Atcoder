S = input()
row = [1,1,1,1,1,1,1]
if S[0] == '1':
    print('No')
    exit()
if S[6] == '0':
    row[0] = 0
if S[3] == '0':
    row[1] = 0
if S[1] == '0' and S[7] == '0':
    row[2] = 0
if S[0] == '0' and S[4] == '0':
    row[3] = 0
if S[2] == '0' and S[8] == '0':
    row[4] = 0
if S[5] == '0':
    row[5] = 0
if S[9] == '0':
    row[6] = 0
x = -1
for i in range(7):
    if row[i] == 1:
        x = i
        break
if x == -1 or x >= 5:
    print('No')
    exit()
y = -1
for i in range(x+1,7):
    if row[i] == 0:
        y = i
        break
if y == -1 or y == 6:
    print('No')
    exit()
for i in range(y+1,7):
    if row[i] == 1:
        print('Yes')
        exit()

print('No')