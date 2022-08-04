import math
T = int(input())
L,X,Y = map(int,input().split())
Q = int(input())
for i in range(Q):
    E = int(input())
    y,z = -(L/2)*math.sin(2*E*math.pi/T),-(L/2)*math.cos(2*E*math.pi/T)+L/2
    print(math.degrees(math.atan(z/(X**2+(Y-y)**2)**0.5)))