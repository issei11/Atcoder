import random

def generate():
    with open("input.txt",mode="w")as input_file:
        N = random.randint(3,300)
        M = random.randint(3,N*(N-1)//2)
        input_file.write(f"{N} {M}\n")
        x = [[False] * N for _ in range(N)]
        cnt = 0
        while cnt < M:
            u = random.randint(1,N-1)
            v = random.randint(u+1,N)
            l = random.randint(1,10**5)
            if x[u-1][v-1] == False:
                input_file.write(f"{u} {v} {l}\n")
                x[u-1][v-1] = True
                cnt += 1
    return

generate()


#例
#import random
#
#def generate():
#    with open("input.txt",mode="w")as input_file:
#        a=random.randint(1,100)
#        input_file.write(f"{a}\n")
#        b=random.randint(1,100)
#        c=random.randint(1,100)
#        input_file.write(f"{b} {c}\n")
#        s=[]
#        length=random.randint(1,100)
#        for i in range(length):
#            s.append(chr(random.randint(ord("a"),ord("z"))))
#        s="".join(s)
#        input_file.write(f"{s}\n")
#    return