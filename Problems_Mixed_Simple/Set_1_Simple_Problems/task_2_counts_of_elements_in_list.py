# task_2

def get_counts_of_elements_in_list(some_list):
    result_dict = {}
    for el in some_list:
        if el not in result_dict:
            result_dict[el] = 0
        result_dict[el] += 1

    return result_dict


sample_list = [1, 1, 8, 4, 4, 2, 4, 8]
print(get_counts_of_elements_in_list(sample_list))
