class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_info(self):
        print(f"Студент: {self.name} | Вік: {self.age} | Курс: {self.course}")

    def change_course(self, new_course):
        self.course = new_course
        print(f"[Оновлено] Студент {self.name} перейшов на {new_course} курс.")

print("--- Завдання 1, 2, 3 ---")

student1 = Student("Олександр", 19, 2)
student2 = Student("Анастасія", 21, 4)

student1.show_info()
student2.show_info()

student1.change_course(3)
student1.show_info()  




class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True

print("\n--- Завдання 4, 5 ---")

task1 = Task("Повторити теорію ООП")
task2 = Task("Виконати домашку з Python")
task3 = Task("Здати роботу на перевірку")

task2.mark_done()

tasks_list = [task1, task2, task3]

for index, task in enumerate(tasks_list, 1):
    status = " Виконано" if task.completed else " Не виконано"
    print(f"{index}. {task.title} — [{status}]")



class Event:
    def __init__(self, title, date, description="Немає опису"):
        self.title = title
        self.date = date
        self.description = description

    def show(self):
        print(f"\nПодія: {self.title}")
        print(f"Дата: {self.date}")
        print(f"Опис: {self.description}")

    def update_description(self, new_description):
        self.description = new_description


print("\n--- Завдання 6, 7 ---")

my_event = Event("Вебінар з Python", "15.10.2026")
my_event.show() 

my_event.update_description("Розбір складних тем ООП: наслідування та поліморфізм.")

print("\n[Оновлена подія]:")
my_event.show()


