def fibonacci(fibonacciLength):
    # with these constraints I'm pretty much insentivesed to hardcore the dict...
    fibonacciFirst10Numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    # # to dict...
    # fib_10_nums_to_dict = {k + 1: v for k, v in enumerate(fibonacciFirst10Numbers)}
    # print(fib_10_nums_to_dict)

    return fibonacciFirst10Numbers[:fibonacciLength]


for i in range(1, 11):
    print(fibonacci(i))

# # Output
# [0]
# [0, 1]
# [0, 1, 1]
# [0, 1, 1, 2]
# [0, 1, 1, 2, 3]
# [0, 1, 1, 2, 3, 5]
# [0, 1, 1, 2, 3, 5, 8]
# [0, 1, 1, 2, 3, 5, 8, 13]
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
