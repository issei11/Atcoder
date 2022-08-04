s = input()
t = input()
s = sorted(s)
t = sorted(t)
print("Yes" if s < t[::-1] else "No")
#2022/6/7 00:04:24