import random

def generate():
    with open("input.txt",mode="w")as input_file:
        W = random.randint(9998,10000)
        input_file.write(f"{W}\n")
        N = random.randint(49,50)
        K = random.randint(49,50)
        if K > N:
            N,K = K,N
        input_file.write(f"{N} {K}\n")
        cnt = 0
        while cnt < N:
            A = random.randint(900,1000)
            B = random.randint(90,100)
            input_file.write(f"{A} {B}\n")
            cnt += 1
    return

generate()


#import random
#
#def generate():
#    with open("input.txt",mode="w")as input_file:
#        N = random.randint(1,50)
#        input_file.write(f"{N}\n")
#        x = [False for _ in range(N)]
#        cnt = 0
#        while cnt < N:
#            tmp = random.randint(1, N)
#            if x[tmp-1] == False:
#                print(tmp)
#                input_file.write(f"{tmp}\n")
#                x[tmp-1] = True
#                cnt += 1
#    return
#
#generate()

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