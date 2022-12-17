#Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

word = input('Введите слово, которое нужно удалить: \n')
string = input ('Введите строку для фильтрации: \n')
split_str = string.split()
filtered_str = ' '.Join((filter(lambda s: word not in s, split_str)))
print("Отфильтрованная строка: ", filtered_str)