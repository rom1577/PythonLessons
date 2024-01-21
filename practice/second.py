# Программа по определению длины самого длинного слова в строке
s = input("Введите строку: ")

current_len = 0  # длина текущего слова
max_len = 0  # длина максимального слова 

for i in range(len(s)):
    if s[i] == ' ':
        current_len = 0
        continue
    current_len += 1
    if current_len > max_len:
        max_len = current_len

print("Максимальная длина слова равна ", max_len) 
