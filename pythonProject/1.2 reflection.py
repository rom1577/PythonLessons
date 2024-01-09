'''
Моя схема организации классов схожа с эталонным решением.
Однако, я заполнил не все поля - оставил в классе Dwarf и Animal непроициниализированные массивы и строки,
но заполнил их при работе с объектами.

Считаю, что в классе Animal поля
    lay_eggs = True  # Способно ли нести яйца
    train = True  # Поддается ли дрессировке
не должны быть полями, т.к класс должен характеризовать конкретную сущность. Считаю правильнее было создать
отдельно классы для животных, способных нести яйца и нет (аналогично с дрессировкой).

'''