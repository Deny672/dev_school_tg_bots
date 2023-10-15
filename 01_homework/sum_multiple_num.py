"""
https://www.codewars.com/kata/514b92a657cdc65150000006
"""

def task(num):
    sum = 0
    while num > 0:
        num -= 1
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum


number = int(input('Введіть ваше число '))
print(task(number))