'''
Дано трехзначное число. Найдите сумму его цифр.
'''

number = int(input())
print((number // 100) + (number // 10 % 10) + (number % 10))
