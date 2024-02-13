import os
from PIL import Image

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

# функция конвертации изображения в другой формат
def func(oldExp, newExp):
    # получаем список файлов и директорий
    l = scan_dir(".", oldExp, False)
    if len(l[0]) == 0:
        return
    for k in l[0]:
        with Image.open(k) as im:
            im.save(k.split(".")[0] + newExp)
            os.remove(k.split(".")[0] + oldExp)


