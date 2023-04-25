# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

numberOne = int(input("Enter number # 1: "))
numberTwo = int(input("Enter number # 2: "))

def recr (a, b):
   if b == 0 :
        return a
   return recr(a, b - 1) + 1
print (f"Если к числу {numberOne} прибавить число {numberTwo} = > {recr(numberOne, numberTwo)}")
