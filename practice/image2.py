import os
from PIL import Image, ImageDraw

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

# функция конвертации изображения в другой формат и рисования квадрата
def func2(oldExp, newExp):
    l = scan_dir(".", oldExp, False)
    if len(l[0]) == 0:
        return
    param = 100  # сторона квадрата в пикселях
    for k in l[0]:
        with Image.open(k) as im:  # открытие файла
            assert (param <= im.size[0])  # проверка чтобы сторона квадрата не была больше размера рисунка
            assert (param <= im.size[1])
            draw = ImageDraw.Draw(im)
            # черчение квадрата
            draw.rectangle([im.size[0] / 2 - param / 2, im.size[1] / 2 - param / 2, im.size[0] / 2 + param / 2,
                            im.size[1] / 2 + param / 2], outline=(0,0,0), width=5)
            im.save(k.split(".")[0] + newExp)
            os.remove(k.split(".")[0] + oldExp)