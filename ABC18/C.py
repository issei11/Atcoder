R,C,K = map(int,input().split())
#しゃくとり法で実装
map = [input() for _ in range(R)]

check = [[0]*(2*K-1) for _ in range(2*K-1)]



cnt = 0
