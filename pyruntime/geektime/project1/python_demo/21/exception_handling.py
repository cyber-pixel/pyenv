
# NameError: name 'j' is not defined
#i = j

# SyntaxError: invalid syntax  语法错误
#print())

# IndexError: string index out of range
# a='123'
# print(a[3])

# KeyError: 'c'
# d = {'a':1 ,'b':2}
# print(d['c'])

# ValueError: invalid literal for int() with base 10: 'abc'
#year = int(input('input year:'))

# 捕获异常
# try:
#     year = int(input('input year:'))
# except ValueError:
#     print('年份要输入数字')


# AttributeError: 'int' object has no attribute 'append'
# a=123
# a.append()

# except (ValueError, AttributeError, KeyError)

# ZeroDivisionError: division by zero
# print(1/0)

# 输出错误信息 e，Exception捕获全部信息
# try:
#     print(1/'a')
# except Exception as e:
#     print(' %s' %e)

# 自定义错误提示信息
# try:
#     raise NameError('helloError')
# except NameError as e:
#     print('my custom error %s' %e)


try:
    a = open('name.txt')
except Exception as e:
    print(e)

finally:
    a.close()



