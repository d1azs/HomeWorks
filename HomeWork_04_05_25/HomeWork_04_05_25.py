from datetime import date

class StaffMember:
    def __init__(self, name, staff_id, hire_date=None, salary=None):
        self.name = name
        self.staff_id = staff_id
        self.hire_date = hire_date
        self.salary = salary

    def show_info(self):
        info = f"Ім’я: {self.name}\nID: {self.staff_id}"
        if self.hire_date:
            info += f"\nДата найму: {self.hire_date}"
        if self.salary:
            info += f"\nЗарплата: {self.salary} грн"
        return info

class LoginMixin:
    def login(self):
        return f"{self.name} увійшов у систему."

    def logout(self):
        return f"{self.name} вийшов із системи."

class ScheduleMixin:
    def set_schedule(self, days):
        self.schedule = days

    def show_schedule(self):
        if hasattr(self, 'schedule'):
            return f"Графік роботи: {', '.join(self.schedule)}"
        return "Графік роботи не встановлений."

class Chef(StaffMember, LoginMixin, ScheduleMixin):
    def __init__(self, name, staff_id, hire_date=None, salary=None, specialty=None):
        super().__init__(name, staff_id, hire_date, salary)
        self.specialty = specialty
        self.dishes = []

    def add_dish(self, dish_name):
        self.dishes.append(dish_name)

    def show_duties(self):
        duties = [f"Приготування страв за спеціалізацією: {self.specialty}"]
        duties.extend([f"Приготування страви: {dish}" for dish in self.dishes])
        return duties

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}\nПосада: Шеф-кухар\nСпеціалізація: {self.specialty}"

class Waiter(StaffMember, LoginMixin, ScheduleMixin):
    def __init__(self, name, staff_id, hire_date=None, salary=None, service_zone=None):
        super().__init__(name, staff_id, hire_date, salary)
        self.service_zone = service_zone
        self.tables = []

    def assign_table(self, table_number):
        self.tables.append(table_number)

    def show_duties(self):
        duties = [f"Обслуговування зони: {self.service_zone}"]
        duties.extend([f"Обслуговування столика №{table}" for table in self.tables])
        return duties

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}\nПосада: Офіціант\nЗона обслуговування: {self.service_zone}"

if __name__ == '__main__':
    chef = Chef(name="Тимофій", staff_id=101, hire_date="04-05-2025", salary=35000, specialty="Італійська кухня")
    chef.set_schedule(["Понеділок", "Середа", "П'ятниця"])
    chef.add_dish("Паста карбонара")
    chef.add_dish("Маргарита")
    print(chef.login())
    print(chef.show_info())
    print(chef.show_schedule())
    print("Обов’язки шефа:")
    for duty in chef.show_duties():
        print("-", duty)
    print(chef.logout())