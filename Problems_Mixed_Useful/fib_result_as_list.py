def fibonacci(fibonacciLength):
    result = [0]

    if fibonacciLength == 1:
        return result

    result.append(1)
    if fibonacciLength == 2:
        return result

    if fibonacciLength > 2:
        for _ in range(fibonacciLength - 2):
            result.append(result[-1] + result[-2])

    return result


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
