class Fibonacci:
    def __init__(self):
        self.cache = {0: 0, 1: 1}

    def __call__(self, n):
        # if n not in self.cache:
        #     if n == 0 or n == 1:
        #         self.cache[n] = n
        #     else:
        #         self.cache[n] = self(n - 1) + self(n - 2)
        #
        # return self.cache[n]

        if n not in self.cache:
            for i in range(2, n + 1):
                if i not in self.cache:
                    self.cache[i] = self.cache[i - 1] + self.cache[i - 2]

        return self.cache[n]


fib = Fibonacci()

for i in range(6):
    print(fib(i))

print(fib(8))
print(fib(6))
print(fib.cache)
