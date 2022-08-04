class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.height = [0 for _ in range(n)]
    def get_root(self,i):
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self.get_root(self.parent[i])
            return self.parent[i]
    def unite(self,i,j):
        root_i = self.get_root(i)
        root_j = self.get_root(j)
        if root_i != root_j:
            if self.height[root_i] < self.height[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                if self.height[root_i] == self.height[root_j]:
                    self.height[root_i] += 1
    def is_in_group(self,i,j):
        if self.get_root(i) == self.get_root(j):
            return True
        else:
            return False

def Kruskal(V,e_list):
    e_cost_sorted = []

    for e in e_list:
        e_cost_sorted.append([e[2],e[0],e[1]])
    e_cost_sorted = sorted(e_cost_sorted,reverse=True)

    uf_tree = UnionFind(V)
    mst = []
    s = 0
    for e in e_cost_sorted:
        print(e)
        if not uf_tree.is_in_group(e[1],e[2]):
            print("Yes")
            uf_tree.unite(e[1],e[2])
            mst.append([e[1],e[2]])
            s += e[0]
            print(s)
    return s

N = int(input())
C = list(map(int,input().split()))
W = list(map(int,input().split()))

edges_list = []
for i in range(N):
    for j in range(i+1,N):
        if C[i] == C[j]:
            e = W[i]+W[j]
            edges_list.append([i,j,e])
            edges_list.append([j,i,e])
        else:
            e = -(W[i]+W[j])
            edges_list.append([i,j,e])
            edges_list.append([j,i,e])

print(Kruskal(N,edges_list))