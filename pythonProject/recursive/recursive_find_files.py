import os

def find_files(directory: str)->list:
    List = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)  # Полный путь
        if os.path.isdir(item_path):
            # Если объект папка, то вызываем функцию снова и добавляем результат к списку
            List.extend(find_files(item_path))
        else:
            List.append(item_path)
    return List

