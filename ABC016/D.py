import copy

def intersect(p1, p2, p3, p4):
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return tc1*tc2<0 and td1*td2<0

Ax,Ay,Bx,By = map(int,input().split())
A = [Ax,Ay]
B = [Bx,By]
N = int(input())
p_prev = list(map(int,input().split()))
cnt = 0
for _ in range(1,N):
    p_next = list(map(int,input().split()))
    if intersect(A,B,p_prev,p_next):
        cnt += 1
    p_prev = copy.deepcopy(p_next)
print((cnt+1)//2+1)
#2022/8/3 00:20:36