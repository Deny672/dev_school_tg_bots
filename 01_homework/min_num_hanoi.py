"""
https://www.codewars.com/kata/534eb5ad704a49dcfa000ba6
"""
def search_count_move(count_disk):
    return (2 ** count_disk) - 1

a = 10
print(search_count_move(a))