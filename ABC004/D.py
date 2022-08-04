R,G,B = map(int,input().split())
max_color = max(R,G,B)
ans = 0
if max_color == R:
    if R > 198:
        if R%2 == 0:
            ans += (R//2+1)*(R//2)-R//2
        else:
            ans += (R//2+1)*(R//2)
        
