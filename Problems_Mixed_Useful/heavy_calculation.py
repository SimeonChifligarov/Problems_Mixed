def heavy_calculation(*args):
    return sum(*args)


def calculate(*args, memo=None):
    if memo is None:
        memo = {}
        
    arguments = args
    try:
        value = memo[arguments]  # return already calculated value
    except KeyError:
        value = heavy_calculation(arguments)
        memo[arguments] = value  # update the memo dictionary
    return value


print(calculate(3, 4, 5))
print(calculate(3, 2))
print(calculate(3, 3, 5))
print(calculate(3, 4, 5))
print(calculate(3, 2))
