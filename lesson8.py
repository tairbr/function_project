# def my_func(n):
#     sum = 1
#     for i in (1,n):
#         sum = i * (i-1)
#     return sum
#
# print(my_func(5))


# def my_format (string, char='!'):
#     result_string = f'{char} {string} {char}'
#     return result_string
# print(my_format('foto', char='#'))

# def my_pow(number, power):
#     resualt = number**

# def print_list(*args):
#     print(type(args))
# print_list(1, 2, 3, 4, 5)

def print_list(*args):
    summ = 0
    n = 0

    for i in args:
        summ += args[n]*i
        n += 1
    print(summ)
print_list(1, 2, 3)