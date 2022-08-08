S = input()
sound = ['Do','Re','Mi','Fa','So','La','Si']
if S[:12] == 'WBWBWWBWBWBW':
    print(sound[0])
elif S[:12] == 'WBWWBWBWBWWB':
    print(sound[1])
elif S[:12] == 'WWBWBWBWWBWB':
    print(sound[2])
elif S[:12] == 'WBWBWBWWBWBW':
    print(sound[3])
elif S[:12] == 'WBWBWWBWBWWB':
    print(sound[4])
elif S[:12] == 'WBWWBWBWWBWB':
    print(sound[5])
elif S[:12] == 'WWBWBWWBWBWB':
    print(sound[6])
#2022/8/8 00:05:55