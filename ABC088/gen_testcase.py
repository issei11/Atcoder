import random

def generate():
    with open("input.txt",mode="w")as input_file:
        H = random.randint(2,20)
        W = random.randint(2,20)
        input_file.write(f"{H} {W}\n")
        s = ''
        for i in range(H):
            for j in range(W):
                if (i == 0 and j == 0) or (i == H-1 and j == W-1):
                    s = s+'.'
                else:
                    x = random.randint(1,10)
                    if x < 3:
                        s = s+'#'
                    else:
                        s = s+'.'
            input_file.write(f"{s}\n")
            s = ''
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