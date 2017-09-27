# coding:utf-8
# 测试map函数的用法

'''
Docstring:
map(function, sequence[, sequence, ...]) -> list
Return a list of the results of applying the function to the items of
the argument sequence(s).  If more than one sequence is given, the
function is called with an argument list consisting of the corresponding
item of each sequence, substituting None for missing values when not all
sequences have the same length.  If the function is None, return a list of
the items of the sequence (or a list of tuples if more than one sequence).

从map函数的文档中可以看出，该函数的第一个参数为一个函数对象，后面可以跟一个或多个序列，函数的返回值是一个list.

如果函数不为None，那么返回的结果list的第i个元素，是将该函数作用于每个序列的第i个元素的结果。如果传入的序列的长度不都是相同的，
那么结果list的某些元素将会是None.

如果函数为None，那么返回的的结果list的第i个元素，是每个序列第i个元素组成的n元组（n为序列的个数），如果每个序列的长度不都是相同的，那么结果list
的某些元素将是None.
'''

def main():
    a = [1,2,3,4]
    b = [3,5,9]
    c = [8,2,3]
    print map(None,a,b,c)
    # 输出：[(1, 3, 8), (2, 5, 2), (3, 9, 3), (4, None, None)]

    print map(lambda x : x ** 2,a)
    # 输出：[1, 4, 9, 16]

    # print map(lambda x,y : x + y,a)
    # 输出：TypeError <lambda>() takes exactly 2 arguments (1 given)

    print map(lambda x,y : x + y,b,c)
    # 输出：[11, 7, 12]

    # print map(lambda x,y,z : x + y + z,a,b,c)
    # 输出：TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

    print map(lambda x,y : x + y if x is not None and y is not None else None,a,b)
    # 输出：[4, 7, 12, None]

if __name__ == '__main__':
    main()