# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# Любое действие выводит сумму денег
import sys

BALANCE = 0
COUNT = 0
RICHLIMIT = 5_000_000
RICHTAX = 0.1
BONUSRATE = 0.03
FREENDERING = 0.015


def add_money():
    global COUNT, BALANCE
    money = int(input('Введите сумму пополнения, кратную 50 у.е.'))
    if money % 50 == 0:
        BALANCE += money
        print(f'Вы пополнили счет на {money} у.е.\n'
              f'Баланс составляет {BALANCE} у.е')
        COUNT += 1.
    else:
        print('Сумма пополнения не кратно 50 у.е.')


def get_money() -> int:
    global COUNT, BALANCE, FREENDERING
    withdrow = int(input('Введите сумму снятия, кратную 50 у.е.'))
    if withdrow > BALANCE:
        print('Запрашиваемая сумма, больше чем сумма на счете')
    elif withdrow % 50 == 0:
        if withdrow * FREENDERING < 30:
            rate = 30
        elif withdrow * FREENDERING > 600:
            rate = 600
        else:
            rate = withdrow * FREENDERING
        BALANCE = BALANCE - withdrow - rate
        print(f'Вы сняли со счета {withdrow}, проценты за снятие {rate} у.е.\n'
              f'Баланс составляет {BALANCE} у.е')
        COUNT += 1
    else:
        print('Сумма снятия не кратна 50 у.е.')


def add_bonus():
    global BONUSRATE, BALANCE
    BONUSSUM = BALANCE * BONUSRATE
    BALANCE += BALANCE * BONUSRATE
    print(f'Начислен бонус {BONUSSUM}')


while True:
    action = input('Введите операцию 1,2,3: ')
    if BALANCE > RICHLIMIT:
        TAX = BALANCE * RICHTAX
        BALANCE -= TAX
        print(f'С вас списали налог на богатство в размере {TAX}')

    match action:
        case '1':
            add_money()
        case '2':
            get_money()
        case '3':
            print(f'Баланс составляет {BALANCE} у.е')
            sys.exit()

    if COUNT % 3 == 0:
        add_bonus()
    else:
        pass
