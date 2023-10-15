"""
These assignments are taken by the course creators from CodeWars, here's a link to learn the essence of the assignment
https://www.codewars.com/kata/5679aa472b8f57fb8c000047
"""
def check_sum(arr):
    for i in range(len(arr)):
        sum_to_i = 0
        sum_after_i = 0
        for k in range(i):
            sum_to_i += arr[k]

        for j in range(i+1, len(arr)):
            sum_after_i += arr[j]

        if sum_to_i == sum_after_i:
            return i
    return -1

arr = [1, 100, 50, -51, 1, 1]
print(check_sum(arr))