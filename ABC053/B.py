s = input()
idx_a = -1
idx_z = 0
for i in range(len(s)):
    if s[i] == 'A' and idx_a == -1:
        idx_a = i
    elif s[i] == 'Z' and idx_z < i:
        idx_z = i
print(idx_z-idx_a+1)
#2022/8/14 00:04:33 1WA