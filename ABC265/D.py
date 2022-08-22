N,P,Q,R = map(int,input().split())
A = list(map(int,input().split()))
p_s = 0
p_e = 0
S_p = A[0]
q_s = 0
q_e = 0
S_q = A[0]
r_s = 0
r_e = 0
S_r = A[0]
while p_e < N:
    if S_p < P:
        if p_e == N-1:
            print('No')
            exit()
        p_e += 1
        S_p += A[p_e]
    elif S_p == P:
        while q_e < N:
            if S_q < Q:
                if q_e == N-1:
                    print('No')
                    exit()
                q_e += 1
                S_q += A[q_e]
            elif S_q == Q:
                if p_e+1 == q_s:
                    while r_e < N:
                        if S_r < R:
                            if r_e == N-1:
                                print('No')
                                exit()
                            r_e += 1
                            S_r += A[r_e]
                        elif S_r == R:
                            if q_e+1 == r_s:
                                print('Yes')
                                exit()
                            elif q_e+1 < r_s:
                                q_e += 1
                                break
                            elif q_e+1 > r_s:
                                S_r -= A[r_s]
                                r_s += 1
                        elif S_r > R and r_s < r_e:
                            S_r -= A[r_s]
                            r_s += 1
                        elif S_r > R and r_s == r_e:
                            if r_e == N-1:
                                print('No')
                                exit()
                            r_s += 1
                            r_e += 1
                            S_r = A[r_s]
                    q_e += 1
                    S_q += A[q_e]
                elif p_e+1 < q_s:
                    p_e += 1
                    break
                elif p_e+1 > q_s:
                    S_q -= A[q_s]
                    q_s += 1
            elif S_q > Q and q_s < q_e:
                S_q -= A[q_s]
                q_s += 1
            elif S_q > Q and q_s == q_e:
                if q_e == N-1:
                    print('No')
                    exit()
                q_s += 1
                q_e += 1
                S_q = A[q_s]
        p_e += 1
        S_p += A[p_e]
    elif S_p > P and p_s < p_e:
        S_p -= A[p_s]
        p_s += 1
    elif S_p > P and p_s == p_e:
        if p_e == N-1:
            print('No')
            exit()
        p_s += 1
        p_e += 1
        S_p = A[p_s]

print('No')