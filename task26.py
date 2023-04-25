# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

number = int(input("Enter number: "))
degree = int(input("Enter degree of number: "))

def recr (a, b):
   count = b
   if count == 0:
        return a
   count -=1 
   return (a**b)
print (f"Число {number} в степени {degree} = > {recr(number, degree)}")
 