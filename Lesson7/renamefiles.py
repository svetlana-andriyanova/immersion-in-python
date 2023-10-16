# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце
#   имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно
#   работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
#   Например,для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени
#   файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее
#   счётчик файлов и расширение

from createfiles import create_files
import os


def group_rename(new_name, digits, origin_ext, end_ext, range_name, path='.'):
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith(origin_ext):
            initial_name = os.path.splitext(filename)[0]
            if range_name:
                initial_name_str = initial_name[range_name[0]:range_name[1]]
            else:
                initial_name_str = ""
            new_filename = f"{initial_name_str}{new_name}" \
                           f"{str(counter).zfill(digits)}{end_ext}"
            os.rename(os.path.join(path, filename),
                      os.path.join(path, new_filename))
            counter += 1


if __name__ == '__main__':
    create_files(r'D:\GB\pythonProject\Lesson7', '.txt', 3)
    create_files(r'D:\GB\pythonProject\Lesson7', '.json', 2)
    create_files(r'D:\GB\pythonProject\Lesson7', '.jpeg', 1)

    group_rename('_rename_', 3, '.txt', '.md', [0, 2],
                 r'D:\GB\pythonProject\Lesson7')
