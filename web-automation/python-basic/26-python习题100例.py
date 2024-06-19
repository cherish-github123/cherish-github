"""
1.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
解析：三位数字，个 十 百, 1,2,3,4都可以填写
"""
num=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=k and i!=j and j!=k:
                num.append(i*100+j*10+k)
                print(num)
                print(len(num))

"""

"""

