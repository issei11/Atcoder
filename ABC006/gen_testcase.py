import random

def generate():
    with open("input.txt",mode="w")as input_file:
        N = random.randint(1,100)
        input_file.write(f"{N}\n")
        x = [False for _ in range(N)]
        cnt = 0
        while cnt < N:
            tmp = random.randint(1, N)
            if x[tmp-1] == False:
                print(tmp)
                input_file.write(f"{tmp}\n")
                x[tmp-1] = True
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