N = int(input())

s = [0]
t = [0]
for i in range(N):
    S, T = input().split()
    s.append(S)
    t.append(T)

frag = True

for i in range(1,N+1):
    for j in range(1,N+1):
        if (s[i] == s[j] or s[i] == t[j]) and i != j:#not s[i] = a[i]
            for k in range(1,N+1):
                if (t[i] == s[k] or t[i] == t[k]) and i != k:
                    print("No")
                    frag = False
                    break
            else:
                continue
            break
    else:
        continue
    break

if frag:
    print("Yes")
#2022/4/19 00:32:03