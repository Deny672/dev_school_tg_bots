def largest_radial_sum(arr, d):
    step = len(arr) // d
    sum_list = []
    for i in range(step):
        sublist = arr[i::step]
        sublist_sum = sum(sublist)
        sum_list.append(sublist_sum)

    max_sum = max(sum_list)
    return max_sum

arr = [1, 5, 6, 3, 4, 2]
count = 3
print(largest_radial_sum(arr, count))

# k = int(len(arr) / count_group)
# rating_group = {}
# value_rating_group = []
# for i in range(k):
#     for j in range(count_group):
#         if j in rating_group:
#             rating_group[j] += arr[j + count_group * i]
#         else:
#             rating_group[j] = arr[j + count_group * i]
# for key in range(len(rating_group)):
#     value_rating_group.append(rating_group[key])
# return max(value_rating_group)
