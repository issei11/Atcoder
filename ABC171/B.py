N,K = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
p_ans = p[:K]
print(sum(p_ans))
#2022/6/6 00:01:50