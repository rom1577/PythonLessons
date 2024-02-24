import os
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont

# функция поиска файла в директории
def scan_dir(path, ext, fil):
    files = []
    dirs = []
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path,f)):
            dirs.append(f)
        else:
            if ext == ".*" or f.endswith(ext):
                files.append(f)

    if(fil):
       f1 = []
       d1 = []
       for d in dirs:
           res = scan_dir(os.path.join(path,d), ext, False)
           f1.extend(res[0])
           d1.extend(res[1])

       files.extend(f1)
       dirs.extend(d1)

    return [files, dirs]

# функция конвертации изображения в другой формат, рисование квадрата и написания текста
def func2(oldExp, newExp):
    l = scan_dir(".",oldExp,False)
    if len(l[0]) == 0:
        return

    for k in l[0]:
        param = 100  # сторона квадрата в пикселях
        with Image.open(k) as im:  # открытие файла
            if param > im.size[0] or param > im.size[1]:
                param = min(im.size[0], im.size[1]) // 2
            draw = ImageDraw.Draw(im)  # создание холста
            # задание массивов положения
            ar_rectangle = [im.size[0] // 2 - param // 2, im.size[1] // 2 - param // 2, im.size[0] // 2 + param // 2,
                            im.size[1] // 2 + param // 2]
            ar_text = [im.size[0] // 2 - param // 2, im.size[1] // 2 - param // 2 + round(2/3*param),
                       im.size[0] // 2 + param//2, im.size[1] // 2 + param // 2]
            # рисование прямоугольника
            draw.rectangle(ar_rectangle, outline=(0,0,0), width=5)
            # написание текста
            draw.multiline_text(ar_rectangle,"Hello,", fill=(0,0,0), spacing=param/3, font_size = param/3)
            draw.multiline_text(ar_text, "World!", fill=(0, 0, 0), spacing=param / 3, font_size=param / 3)
            # сохранение рисунка в новом формате
            im.save(k.split(".")[0] + newExp)
            del draw  # удаление холста
            os.remove(k.split(".")[0] + oldExp)  # удаление файла со старым расширением
func2(".JPEG",".PNG")

