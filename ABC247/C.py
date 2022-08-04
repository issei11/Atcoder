def generate(N):
    S = [1]
    if N == 1:
        return(S)
    N_list = [N]
    return(generate(N-1)+N_list+generate(N-1))

N = int(input())
print(*generate(N))

#2022/4/19 00:08:57