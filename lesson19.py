class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def show(self):
        print(f"Подія: {self.title} | Дата: {self.date}")

    def get_info(self):
        return f"[Event] Назва: {self.title}, Дата: {self.date}"

class Training(Event):
    def __init__(self, title, date, coach):
        super().__init__(title, date)
        self.coach = coach  

    def show(self):
        print(f"Тренування: {self.title} | Дата: {self.date} | Тренер: {self.coach}")

    def get_info(self):
        return f"[Training] Назва: {self.title}, Дата: {self.date}, Тренер: {self.coach}"


class Birthday(Event):
    def __init__(self, title, date, age):
        super().__init__(title, date)
        self.age = age  

    def show(self):
        """Перевизначений метод show()."""
        print(f"День народження: {self.title} | Дата: {self.date} | Виповнюється років: {self.age}")

    def get_info(self):
        return f"[Birthday] Іменинник: {self.title}, Дата: {self.date}, Вік: {self.age}"


class OnlineEvent(Event):
    def __init__(self, title, date, link):
        super().__init__(title, date)
        self.link = link 

    def show(self):
        print(f"Онлайн-подія: {self.title} | Дата: {self.date} | Посилання: {self.link}")

    def get_info(self):
        return f"[Online] Назва: {self.title}, Дата: {self.date}, Посилання: {self.link}"


if __name__ == "__main__":

    events = [
        Event("Збори мешканців", "12.07.2026"),
        Training("Інтенсив з Python", "15.07.2026", "Олексій"),
        Birthday("Максим", "20.07.2026", 25),
        OnlineEvent("Вебінар по ООП", "22.07.2026", "https://zoom.us")
    ]

    print("--- Перевірка ДЗ 3 (Виведення через цикл методом show()) ---")
    for event in events:
        event.show()

    print("\n--- Перевірка ДЗ 4 (Виведення результату методу get_info() окремо) ---")
    for event in events:
        info_string = event.get_info()
        print(f"Отримано рядок -> {info_string}")

