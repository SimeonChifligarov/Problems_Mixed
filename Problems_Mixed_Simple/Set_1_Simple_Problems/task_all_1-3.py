# task_1

# STARTING_NUMBER = 1
# END_NUMBER = 5
# END_MESSAGE = 'DONE'
#
# result = []
#
# i = STARTING_NUMBER
# while i <= END_NUMBER:
#     result.append(str(i))
#     i += 1
#
# result.append(END_MESSAGE)
# print('\n'.join(result))

# task_2
# def get_counts_of_elements_in_list(some_list):
#     result_dict = {}
#     for el in some_list:
#         if el not in result_dict:
#             result_dict[el] = 0
#         result_dict[el] += 1
#
#     return result_dict
#
#
# sample_list = [1, 1, 8, 4, 4, 2, 4, 8]
# print(get_counts_of_elements_in_list(sample_list))

# task_3
# def generate_dict_with_counts(some_list):
#     result_dict = {}
#
#     for word in some_list:
#         if word not in result_dict:
#             result_dict[word] = 0
#         result_dict[word] += 1
#
#     return result_dict
#
#
# def generate_horizontal_histogram(some_dict):
#     result = []
#     for key, value in some_dict.items():
#         current_string = f'{key}|{"*" * value}'
#         result.append(current_string)
#
#     return result
#
#
# list_of_words = ["luxuriant", "silly", "dizzy", "frightening", "blink", "silly", "enjoy",
#                  "suspend", "blink", "reward", "blink", "fact", "debt", "marble", "blink", "yak",
#                  "frightening", "suspend", "debt"]
#
# # print(generate_dict_with_counts(list_of_words))
# # print(generate_horizontal_histogram(generate_dict_with_counts(list_of_words)))
# 
# print('\n'.join(generate_horizontal_histogram(generate_dict_with_counts(list_of_words))))
