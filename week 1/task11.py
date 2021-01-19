"""
Пирожок в столовой стоит A рублей и B копеек.
Определите, сколько рублей и копеек нужно заплатить за N пирожков.
"""
ruble = int(input())
cop = int(input())
count_of_things = int(input())

result = (ruble * 100 + cop) * count_of_things
print((result // 100), (result % ((result // 100) * 100)))
