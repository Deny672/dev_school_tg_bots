"""
https://www.codewars.com/kata/537400e773076324ab000262
"""

def groupAnagrams(arr):
    result = []
    result_4_letter = []
    result_3_letter = []
    result_n_letter = []
    for i in range(len(arr)):
        k = 0
        for j in 'tsar':
            if arr[i].count(j) == 1:
                 k += 1
        if k == 4:
            result_4_letter.append(arr[i])
        elif k == 3:
            result_3_letter.append(arr[i])
        else:
            result_n_letter.append(arr[i])
    result.append(result_4_letter)
    result.append(result_3_letter)
    result.append(result_n_letter)
    return result

input_arr = ["tsar", "rat", "tar", "star", "tars", "cheese"]
print(groupAnagrams(input_arr))