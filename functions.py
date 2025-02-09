def read_znach(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено")
        return ''
