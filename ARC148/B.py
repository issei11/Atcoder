N = int(input())
S = input()

if N == 1:
    print('d')
    exit()
idx = 0
while idx < N:
    if S[idx] == 'p':
        break
    idx += 1

L = idx
if L == N:
    print(S)
    exit()
max_p = 0
R_list = [idx]
tmp_p = 0
cnt = 0
ans2 = ['p']
while idx < N:
    if S[idx] == 'p':
        tmp_p += 1
    else:
        if cnt == 0:
            ans2 = [S[:L]]
            for i in range(tmp_p):
                ans2.append('d')
            ans2.append(S[idx:])
            cnt += 1
        if S[idx-1] == 'p':
            if max_p < tmp_p:
                max_p = tmp_p
                R_list = [idx-1]
            if max_p == tmp_p:
                R_list.append(idx-1)
            tmp_p = 0
    idx += 1

if max_p < tmp_p:
    max_p = tmp_p
    R_list = [idx-1]
if max_p == tmp_p:
    R_list.append(idx-1)

ans = [''.join(ans2)]
for R in R_list:
    ans_tmp = [S[:L]]
    for i in range(R,L-1,-1):
        if S[i] == 'p':
            ans_tmp.append('d')
        else:
            ans_tmp.append('p')
    ans_tmp.append(S[R+1:])
    ans.append(''.join(ans_tmp))
print(min(ans))