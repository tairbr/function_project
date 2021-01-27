def my_func(n):
    sum = 1
    for i in (1,n):
        sum = i * (i-1)
    return sum

print(my_func(5))
