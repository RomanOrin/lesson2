#linefirst= input('Введите первую строку: ')
#linesecond = input('Введите вторую строку: ')

linefirst = 'gigroigjroijg'
linesecond = 5
def string_compare(line1, line2):
    if isinstance(line1, str) and isinstance(line2, str) != True:
        return 0
    elif line1 == line2:
        return 1
    elif line1 != line2 and len(line1) > len(line2):
        return 2
    elif line1 != line2 and line2 == 'learn':
        return 3

print(string_compare(linefirst, linesecond))