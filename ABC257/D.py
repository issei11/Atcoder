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


"class UnionFind:",
"\tdef __init__(self, n):",
"\t\tself.parent = [i for i in range(n)]",
"\t\tself.height = [0 for _ in range(n)] # 各⽊の⾼さ",
"\t",
"\tdef get_root(self, i):",
"\t\tif self.parent[i] == i: # ⾃分が根ノードの場合",
"\t\t\treturn i",
"\t\telse: # 経路圧縮しながら根ノードを探す",
"\t\t\tself.parent[i] = self.get_root(self.parent[i])",
"\t\t\treturn self.parent[i]",
"\t",
"\tdef unite(self, i, j):",
"\t\troot_i = self.get_root(i)",
"\t\troot_j = self.get_root(j)",
"\t\tif root_i != root_j: # より⾼い⽅にマージ",
"\t\t\tif self.height[root_i] < self.height[root_j]:",
"\t\t\t\tself.parent[root_i] = root_j",
"\t\t\telse:",
"\t\t\t\tself.parent[root_j] = root_i",
"\t\t\t\tif self.height[root_i] == self.height[root_j]:",
"\t\t\t\t\tself.height[root_i] += 1",
"\t",
"\tdef is_in_group(self, i, j):",
"\t\tif self.get_root(i) == self.get_root(j):",
"\t\t\treturn True",
"\t\telse:",
"\t\t\treturn False"