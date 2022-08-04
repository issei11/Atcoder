import os
import filecmp

def is_same():
    os.system("python C.py < input.txt > out1.txt")
    os.system("python C_ans.py < input.txt > out2.txt")
    if filecmp.cmp("out1.txt","out2.txt"):
        return True
    else:
        return False

print(is_same())

"""
if is_same() == True:
    print(is_same())
    os.system("python gen_testcase.py ; python exec_testcase.py")
else:
    print(is_same())
"""