"""
https://www.codewars.com/kata/5467e4d82edf8bbf40000155
"""

def sort_num(num):
    arr = []

    for i in str(num):
        arr.append(int(i))


    for i in range(0, len(arr) - 1):
        flag = False
        for x in range(0, len(arr) - 1):
            if arr[x] < arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
                flag = True
        if not flag:
            break
    result = ''
    for i in arr:
        result = result + str(i)
    if len(result) > 2:
        result = result[:-1]
    return int(result)

number = 145263
print(sort_num(number))