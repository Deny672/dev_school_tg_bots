"""
https://www.codewars.com/kata/5839c48f0cf94640a20001d3
"""

def islandPerimeter(arr):
    perimeter = 0
    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == "X":
                perimeter += 4
                if i > 0 and arr[i - 1][j] == "X":
                    perimeter -= 1
                if i < rows - 1 and arr[i + 1][j] == "X":
                    perimeter -= 1
                if j < cols - 1 and arr[i][j + 1] == "X":
                    perimeter -= 1
                if j > 0 and arr[i][j - 1] == "X":
                    perimeter -= 1

    return f"Total land perimeter: {perimeter}"

arr = ['XOOO',
       'XOXO',
       'XOXO',
       'OOXX',
       'OOOO']
print(islandPerimeter(arr))