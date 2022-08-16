class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.height = [0 for _ in range(n)] # 各⽊の⾼さ
    
    def get_root(self, i):
        if self.parent[i] == i: # ⾃分が根ノードの場合
            return i
        else: # 経路圧縮しながら根ノードを探す
            self.parent[i] = self.get_root(self.parent[i])
            return self.parent[i]
    
    def unite(self, i, j):
        root_i = self.get_root(i)
        root_j = self.get_root(j)
        if root_i != root_j: # より⾼い⽅にマージ
            if self.height[root_i] < self.height[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                if self.height[root_i] == self.height[root_j]:
                    self.height[root_i] += 1

    def is_in_group(self, i, j):
        if self.get_root(i) == self.get_root(j):
            return True
        else:
            return False


N = int(input())
x = []
y = []
P = []
for _ in range(N):
    a,b,c = map(int,input().split())
    x.append(a)
    y.append(b)
    P.append(c)

s_need = []
need = 0
for i in range(N):
    for j in range(N):
        if i != j:
            need =(abs(x[i]-x[j])+abs(y[i]-y[j])+P[i]-1)//P[i]
            s_need.append([need,i,j])

s_need.sort()

can_jump = [[i] for i in range(N)]

m = 0
while True:
    can_jump[s_need[m][1]] = can_jump[s_need[m][1]]+can_jump[s_need[m][2]]
    if len(set(can_jump[s_need[m][1]])) == N:
        print(s_need[m][0])
        break
    m += 1
