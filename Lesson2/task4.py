# Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и
# произведение* дробей. Для проверки своего кода используйте модуль fractions.

import math
from fractions import Fraction

frac_str1 = input('Введите первую дробь вида a/b: ')
frac_str2 = input('Введите вторую дробь вида a/b: ')
num1, denom1 = map(int, frac_str1.split("/"))
num2, denom2 = map(int, frac_str2.split("/"))

# Вычисление произведения дробей
prod_num = num1 * num2
prod_denom = denom1 * denom2
prod_frac = (prod_num, prod_denom)
prod_nod = math.gcd(prod_num, prod_denom)
if prod_denom / prod_num != 1:
    prod_fracs = str(int(prod_num / prod_nod)) + '/' \
                 + str(int(prod_denom / prod_nod))
else:
    prod_fracs = str(int(prod_num / prod_denom))
print('Произведение дробей равно', prod_fracs)
# Вычисление произведения дробей (Fraction)
prod_fraction = Fraction(frac_str1) * Fraction(frac_str2)
print('Произведение дробей с помощью Fraction равно', prod_fraction)

# Вычисляем сумму дробей
sum_num = num1 * denom2 + num2 * denom1
sum_denom = denom1 * denom2
sum_nod = math.gcd(sum_num, sum_denom)
if sum_denom / sum_num != 1:
    sum_fracs = str(int(sum_num / sum_nod)) + '/' \
                + str(int(sum_denom / sum_nod))
else:
    sum_fracs = str(int(sum_num / sum_denom))
print('Сумма дробей равна', sum_fracs)
# Вычисление суммы дробей (Fraction)
sum_fraction = Fraction(frac_str1) + Fraction(frac_str2)
print('Сумма дробей с помощью Fraction равно', sum_fraction)
