first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))

second_result = (len(first[z]) == len(second[z]) for z in range(len(first)))


print(list(first_result))
print(list(second_result))
