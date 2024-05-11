"""
迭代器：迭代器是一个可以记住遍历位置的对象
       使用iter()方法创建一个迭代器，使用next()方法依次获取迭代器中的每一个元素，当数组中的元素被遍历完后，抛出StopIteration异常
       迭代器可以使用next()方法依次获取元素，也可以与for循环进行遍历

生成器：使用了yield关键字的函数是一个生成器，是一个返回迭代器的函数，只能用于迭代操作
主要区别：
1.迭代器使用iter()和next()方法实现序列的遍历，生成器使用yield关键字生成值
2.迭代器调用next()方法时返回序列中的下一个元素，生成器返回yield后面的值
3.迭代器遍历完成之后抛出异常
生成器主要用于处理大数据集，因为可以在需要使用时生成值，而不是一次返回
生成器可以用于创建复杂的数据结构，例如斐波那契数列
"""


# TODO 迭代器
list = [8, 3, 5, 66, 5, 9, 5, 34]
it = iter(list)  # 创建一个迭代器
print(it)  # 输出：<list_iterator object at 0x00000220BD260220>，it是一个列表迭代器
print(type(it))    # 输出：<class 'list_iterator'>

# TODO 使用next()方法遍历
# print(next(it))   # 8
# print(next(it))   # 3
# print(next(it))   # 5
# print(next(it))   # 66
# print(next(it))   # 5
# print(next(it))   # 9
# print(next(it))   # 5
# print(next(it))   # 34
# print(next(it))   # 抛出StopIteration异常


# TODO  使用for循环遍历
# for i in it:
#     print(i)



# TODO  生成器
# 定义一个生成器
def f1(n):
    while n > 0:
        yield n
        n -= 1


# 使用这个生成器创建迭代器
generator = f1(10)
# 通过迭代器的next()方法依次获取元素
print(next(generator))   # 10
print(next(generator))  # 9

# TODO  ----------------------使用yield实现斐波那契数列-------------------------------
"""
斐波那契数列：第一位数字和第二位数字是0,1，后面依次是前两位相加的和
斐波那契数列实例： [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
"""
def fibonnacci(n):
    origin_list=[0,1]  # 先将数列的第一个值和第二个值写为0,1
    for i in range(2,n+1):   # 从数列的第三个值开始计算
        print(i)   # i是从2开始
        
        # 当i是2时，是第0位数字+第一位数字，也就是索引为0和为1的数字相加
        # 当i是3时，是第一位数字+第二位数字，也就是索引为1和为2的数字相加
        origin_list.append(origin_list[i-2]+origin_list[i-1])
    return origin_list


print(fibonnacci(11))   #返回[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]




list=[9,89,657,83,7,3,79,5,35,44,78,50]
odd=[]  # 奇数列表
even=[]  # 偶数列表
while len(list)>0:
    number=list.pop()
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)
print(odd)
print(even)


