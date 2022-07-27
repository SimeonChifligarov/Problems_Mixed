def subsetA(arr):
    sorted_array = sorted(arr)
    total_sum_array = sum(sorted_array)

    subset_A = []
    sum_subset_A = 0

    while True:
        if sum_subset_A > total_sum_array:
            break
        current_element = sorted_array.pop()
        subset_A.append(current_element)
        sum_subset_A += current_element
        total_sum_array -= current_element

    return subset_A[::-1]


print(subsetA([3, 7, 5, 6, 2]))
