"""
Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере.
Нельзя пользоваться конкатенацией строк, используйте print с несколькими параметрами.
"""
num = int(input())
n = num + 1
p = num - 1
print("The next number for the number " + str(num) + " is " + str(n) + ".")
print("The previous number for the number " + str(num) + " is " + str(p) + ".")
