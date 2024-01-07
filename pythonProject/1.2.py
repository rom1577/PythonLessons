
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

Beak_Dog = Animal()  # Создание объекта класса Animal - животное Beak_Dog
Beak_Dog.name = "Beak Dog"
Beak_Dog.lay_eggs = True
Beak_Dog.train = False
Beak_Dog.cost = 50
Beak_Dog.body_size_baby = 1500
Beak_Dog.body_size_teen = 50000
Beak_Dog.body_size_adult = 150000
Beak_Dog.edible_parts = ["Мясо","Жир","Мозг","Сердце","Легкие","Кишки","Печень","Почки","Почки",
                         "Желудок","Поджелудочная","Селезенка"]
Beak_Dog.inedible_parts = ["Кости","Череп","Шкура","Гастролит"]

Crosbow = Gun()  # Создание объекта класса Gun - оружие арбалет
Crosbow.name = "Crosbow"
Crosbow.type = "long-range"
Crosbow.distance = 20
Crosbow.produce_materials = ["wood", "metal", "bones"]
Crosbow.damage = 10000

dwarf1 = Dwarf()  # Создание объекта класса Dwarf
dwarf1.status_icon = "Legendary"
dwarf1.conflict_level = "No Quarter"
dwarf1.relationship = ["Супруг", "Божество", "Ученик"]
dwarf1.skill = "Dancer"
dwarf1.emotion = "Agony"
dwarf1.sleep_count = 20000

for i in Beak_Dog.edible_parts:
    print(i)
print(dwarf1.emotion)