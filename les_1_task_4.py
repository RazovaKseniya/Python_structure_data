# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

letter = ord(input('Введите первую букву: '))
letter1 = ord(input('Введите вторую букву: '))

letter = letter - ord('a') + 1
letter1 = letter1 - ord('a') + 1
print(letter, letter1)

letter2 = abs(letter - letter1) - 1
print(f'Между буквами {letter2} символов')