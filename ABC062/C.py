H,W = map(int,input().split())
if H%3 == 0 or W%3 == 0:
    print(0)
else:
    ans = [H,W]
    a = (W//3)*H
    b = (W-W//3)*(H//2)
    c = (W-W//3)*(H-H//2)
    ans.append(max(a,b,c)-min(a,b,c))
    a = (W//3+1)*H
    b = (W-W//3-1)*(H//2)
    c = (W-W//3-1)*(H-H//2)
    ans.append(max(a,b,c)-min(a,b,c))
    a = (H//3)*W
    b = (H-H//3)*(W//2)
    c = (H-H//3)*(W-W//2)
    ans.append(max(a,b,c)-min(a,b,c))
    a = (H//3+1)*W
    b = (H-H//3-1)*(W//2)
    c = (H-H//3-1)*(W-W//2)
    ans.append(max(a,b,c)-min(a,b,c))
    print(min(ans))
#2022/8/22 00:18:25