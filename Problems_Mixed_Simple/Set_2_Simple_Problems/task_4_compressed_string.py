# """
#     Given an input string: "abaabbbc"
#     Group the consecutive occurrences of each character to get "{{a}{b}{aa}{bbb}{c}",
#     in a compressed form: "aba2b3c".
#
#     Implement function compressedString(msg) which returns "aba2b3c" for the input string "abaabbbc"
# """
#

def compressedString(msg):
    result_msg = [msg[0]]
    counter = 1

    for i in range(1, len(msg)):
        current_char = msg[i]

        if current_char == result_msg[-1]:
            counter += 1

            if i == len(msg) - 1:
                result_msg.append(str(counter))

        else:
            if not counter == 1:
                result_msg.append(str(counter))
                counter = 1
            result_msg.append(current_char)

    return ''.join(result_msg)


print(compressedString('abaabbbc'))
print(compressedString('aleeeaalleeee'))
