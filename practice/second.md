# Задание по написанию программы с помощью Far
В данном занятии будет написана программа по подсчету длины слова максимальной длины.
Код программы (сам файл находится [здесь](https://github.com/rom1577/PythonLessons/blob/main/practice/second.py)):
```python
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
```
## Краткий отчет по работе c Far
+ Открывается Far менеджер, в котором создаётся файл `second.py`:

![](https://github.com/rom1577/PythonLessons/blob/main/ScreenShots/far1.JPG)
+ Созданный файл редактируется (меняется кодировка на `UTF-8`) и записывается код программы:

![](https://github.com/rom1577/PythonLessons/blob/main/ScreenShots/far3.JPG)
+ Открывается консоль непосредственно в Far менеджере и выполняется созданный файл:

![](https://github.com/rom1577/PythonLessons/blob/main/ScreenShots/far2.JPG)
