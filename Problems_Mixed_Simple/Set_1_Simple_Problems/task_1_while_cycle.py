# task_1

STARTING_NUMBER = 1
END_NUMBER = 5
END_MESSAGE = 'DONE'

result = []

i = STARTING_NUMBER
while i <= END_NUMBER:
    result.append(str(i))
    i += 1

result.append(END_MESSAGE)
print('\n'.join(result))
