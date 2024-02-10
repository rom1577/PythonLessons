from glob import glob
from zipfile import ZipFile
import os

def zp(fileName, extentsion):
    # удаление архива с с именем fileName, если он существует
    if(os.path.isfile(fileName)):
        os.remove(fileName)
    # создание файла архива с возможностью записи 
    # и выполнение проверки директории на существование файлов с заданным 
    # расширением и запсиь в архив
    with ZipFile(fileName, 'w') as zf:
        for file in glob("*" + extentsion):
            zf.write(file)

zp("arh.zip",".xlsx")
