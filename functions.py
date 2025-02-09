def read_znach(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено")
        return ''


def print_employee_info(name, post, file_write='result.txt'):
    with open(file_write, 'w', encoding='utf-8') as file:
        for name, post in zip(name, post):
            file.write(f'Співробітник {name}, посада - {post}\n')