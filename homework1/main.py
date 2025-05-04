from functions import *

def main():
    print_employee_info(read_znach(input("Введіть назву файлу з іменами: ").strip()),
                        read_znach(input("Введіть назву файлу з посадами: ").strip()))
if __name__ == '__main__':
    main()