
class Animal:  # Класс описывает поля животных в игре Dwarft Fortress
    name = "name"  # Прозвище в игре
    lay_eggs = True  # Способно ли нести яйца
    train = True  # Поддается ли дрессировке
    cost = 500  # Ценность
    body_size_baby = 880  # Размер тела, когда животное ребенок
    body_size_teen = 1000  # Размер тела, когда животное подросток
    body_size_adult = 1200  # Размер тела, когда животное взрослое
    edible_parts = []  # Ссъедобные части
    inedible_parts = []  # Несъедобные части

class Gun:
    name = "name"  # Название оружия
    type = "cutting"  # Тип оружия
    distance = 10  # Дистанция поражения в тайлах
    produce_materials = ["wood","bones"]  # Материалы для изготовления
    damage = 2  # урон от оружия

class Dwarf:
    status_icon = "icon"  # Иконка состояния Дварфа
    conflict_level = "No Quarter"  # Уровни конфликта Дварфа
    relationship = []  # Отношения Дварфа
    skill = ""  # Навык Дварфа
    emotion = ""  # Эмоция Дварфа
    sleep_count = 10000  # Счетчик сонливости Дварфа

dwarf1 = Dwarf()  # Создание объекта класса Dwarf

# Передача объекта по ссылке
dwarf2 = dwarf1
dwarf2.skill = "Comedian"
dwarf1.skill = "Cook"

# Как видно поле skill и для объекта dwarf1 и dwarf2 одинакого и равно "Cook"
# т.к. при присваивании dwarf2 = dwarf1 копируется ссылка на ячейку памяти
print(dwarf1.skill, dwarf2.skill)


