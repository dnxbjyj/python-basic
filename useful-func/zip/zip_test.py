# coding:utf-8
# 测试zip函数

'''
Docstring:
zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]
Return a list of tuples, where each tuple contains the i-th element
from each of the argument sequences.  The returned list is truncated
in length to the length of the shortest argument sequence.

先来看看zip函数的文档，从文档中科院看出，zip函数接收1个或多个序列作为参数，返回一个由元组组成的列表。
结果列表的第i个元素是seq1~seqn的第i个元素组成的元组。
结果列表的长度等于seq1~seqn中最短的序列的长度。
'''

def main():
    a = '1234'
    b = [4,6,7]

    print zip()
    # 输出：[]

    print zip(a)
    # 输出：[('1',), ('2',), ('3',), ('4',)]

    print zip(a,a)
    # 输出：[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]

    print zip(a,[])
    # 输出：[]

    print zip(a,b)
    # 输出：[('1', 4), ('2', 6), ('3', 7)]

if __name__ == '__main__':
    main()