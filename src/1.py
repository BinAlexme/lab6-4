import random
import string
from pathlib import Path

def generate_random_filenames(count, length):
    return [
        ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        for _ in range(count)
    ]

# Указываю папку для сохранения файлов
directory = Path("./trash folder")
directory.mkdir(exist_ok=True)

# генерация 5 случайных файлов с названием и длиной 7 символов
random_filenames = generate_random_filenames(5, 7)

# Создаём пустые файлы
for filename in random_filenames:
    (directory / filename).touch()

# Выводим список всех файлов
for file in directory.iterdir():
    print(file.name, "->", file.absolute())
