import os
import time

directory = '.'

file_path = r'C:\Users\vanq1\PycharmProjects\Python-Lessons\module_7\module_7_5.py'

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = r'C:\Users\vanq1\PycharmProjects\Python-Lessons\module_7\module_7_5.py'
    filetime = os.path.getmtime(file_path)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file_path)
    parent_dir = os.path.dirname(file_path)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
