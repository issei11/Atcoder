N = int(input())
day_time = [0]*289
for _ in range(N):
    s,e = map(int,input().split('-'))
    s = (s//100)*60+s%100
    e = (e//100)*60+e%100
    day_time[s//5] -= 1
    day_time[(e+4)//5] += 1

S = 0
E = 0
raining = 0
sunny = 0
ans = [0,'-',0]
for i in range(289):
    if day_time[i] < 0 and raining == sunny:
        S = ((i*5)//60)*100+(i*5)%60
        raining += abs(day_time[i])
        ans[0] = str(S).zfill(4)
    elif day_time[i] < 0 and raining != sunny:
        raining += abs(day_time[i])
    elif day_time[i] > 0 and raining != sunny+abs(day_time[i]):
        sunny += abs(day_time[i])
    elif day_time[i] > 0 and raining == sunny+abs(day_time[i]):
        E = ((i*5)//60)*100+(i*5)%60
        sunny += abs(day_time[i])
        ans[2] = str(E).zfill(4)
        print(*ans,sep='')
#2022/7/22 00:58:52