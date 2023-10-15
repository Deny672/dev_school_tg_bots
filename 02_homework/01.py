"""
These assignments are taken by the course creators from CodeWars, here's a link to learn the essence of the assignment
https://www.codewars.com/kata/64edf7ab2b610b16c2067579
"""

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

