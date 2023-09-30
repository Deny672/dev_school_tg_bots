"""
In this little assignment you are given a string of space separated
numbers, and have to return the highest and lowest number.
"""
def highAndLow(str):
    arr = str.split(' ')
    for i in range(0, len(arr) - 1):
        flag = False
        for x in range(0, len(arr) - 1):
            if int(arr[x]) > int(arr[x + 1]):
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
                flag = True
        if not flag:
            break
    return arr[-1], arr[0]

text = "1 9 3 4 -5"
print(highAndLow(text))