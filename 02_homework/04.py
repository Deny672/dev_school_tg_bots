
"""
https://www.codewars.com/kata/5fa6d9e9454977000fb0c1f8
"""


def check_track(loot_in_track):
    result = ""
    t = 0
    for i in loot_in_track:
        for j in i:
            if len(j) != 6 or j[0] != '[' or j[-1] != ']':
                continue
            if j[1] == j[2] and j[2] == j[3] and j[3] == j[4]:
                t += 1
                if t == 5:
                    t = 0
                    pass
                else:
                    for k in range(1, 5):
                        result += j[k] + ' '

    if len(result) > 2:
        result = result[:-1]
    return result

loot = [("[IIII]", "[llll]", "[1111]", "[@@@@]", "[||||]", "[║║║║]")]
print(check_track(loot))