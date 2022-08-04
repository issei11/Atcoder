import os
import filecmp

def is_same():
    os.system("python D.py < input.txt > out1.txt")
    os.system("python D_test.py < input.txt > out2.txt")
    if filecmp.cmp("out1.txt","out2.txt"):
        return True
    else:
        return False

print(is_same())