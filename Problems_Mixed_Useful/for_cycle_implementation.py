a = [1, 2, 3, 4, 5, 6]
iter_a = iter(a)
print(iter_a)

while True:
    try:
        element = next(iter_a)
        print(element)
        # print(iter_a)
    except StopIteration:
        break

print(iter_a)  # <list_iterator object at 0x00000149FF1E6140>

iter_b = iter(a)

print(iter_b)  # <list_iterator object at 0x00000149FF1E6200>
