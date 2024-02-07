'''
3.1
Логика решения схожа с эталонным решением. Однако я не использовал цикл для записи
чисел в файл и генерации целых чисел. Использовал другой диапазон цикла. Не уточнил, что
файл открывается для записи в текстовом режиме (символ "t").

3.2
Не разбил функцию на две для разделения логики работы. При подсчете суммы использовал
лишнюю переменную element. Для выявления того, что функция выполнялась с ошибкой, делал
генерацию исключений, вместо кода ошибки, как в эталонном решении. Использовал функцию
rstrip() хотя она тут не нужна, т.к. данные из файла конвертируются в числовой формат,
а не в строку. Данные из файлов преобразовывал в тип float, вместо int, как в эталонном
решении.

3.3
Создал дополнительный цикл для применения функции rstrip(), однако этого делать не
следовало, т.к. символ "\n" появляется только в конце строки, а не после каждого элемента
строки. Использовал лишнюю переменную cats. При обработке исключений использовал
переход на следующий шаг цикла continue, вместо break.
'''
