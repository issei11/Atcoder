N = int(input())

A = 1
B = 1
C = 1
ans = 0
while A*A*A <= N:
    D = N//A
    B = A
    while B*B <= D :
        ans += D//B-B+1
        B += 1
    A += 1

print(ans)