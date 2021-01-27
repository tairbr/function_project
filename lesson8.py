
def fun(*args):
    sum = 0
    a=list(args)
    a.sort()
    print(a[-1])
    for i in args:
        sum += i
    return sum

print(fun(1, 8, 5, 10, 234, 5))