# coding:utf-8
# reduce函数的用法

'''
Docstring:
reduce(function, sequence[, initial]) -> value
Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
of the sequence in the calculation, and serves as a default when the
sequence is empty.

reduce函数接收三个参数：function，seq，init，其中前两个是必选参数，最后一个为可选参数。
reduce函数做了这样一件事情：从左到右遍历seq，将seq[0]和seq[1]传入函数function进行运算（function为一个接收两个参数的函数），得到一个结果值，然后将这个结果值再和
seq[2]传入fucntion进行运算再得到一个新的结果值...以此类推。最终得到一个值，就是该函数的返回值。
如果传入了init，那么init和seq[0]会作为第一次传入funciton的参数，如果seq为空，init也会作为reduce的返回值返回。
'''

def main():
    lst = [1,2,3]
    f = lambda x,y:x*y
    print reduce(f,lst)
    # 输出：6

    print reduce(f,lst,-1)
    # 输出：-6

    print reduce(f,[],-2)
    # 输出：-2

if __name__ == '__main__':
    main()
