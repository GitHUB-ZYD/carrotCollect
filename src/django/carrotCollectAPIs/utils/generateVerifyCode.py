import random
# 用range()
def code(len):
    code_list = []
    for i in range(10):
        code_list.append(str(i))  #生成数字
    for i in range(65, 91):
        code_list.append(chr(i))   #生成大写字母
    for i in range(97, 123):
        code_list.append(chr(i))   #生成小写字母
    r = random.sample(code_list, len)   
    m = ''.join(r)
    return m

