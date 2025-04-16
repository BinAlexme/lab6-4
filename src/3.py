import random
import string
import json


def generate_random_user():
    names = ['cs2govno', 'dark', 'valve', 'hilling', 'pskgu', 'notshit', 'majestic', 'EspScript']
    name = random.choice(names)
    year = random.randint(16, 1337)
    email = f"{name.lower()}{random.randint(1, 100)}@schizophrenia.me"
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(password_chars, k=18))
    user = {
        "name": name,
        "year": year,
        "email": email,
        "password": password
    }
    return user


# Генерирует профиль
user_data = generate_random_user()

# JSON в файл
with open('user.json', 'w') as f:
    json.dump(user_data, f,  indent=4)

# JSON из файла
with open('user.json', 'r') as f:
    loaded_user = json.load(f)

# Вывод
print(json.dumps(loaded_user, indent=4))
