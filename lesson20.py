class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = max(0, initial_balance)

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"[Bank] Успішно внесено {amount}. Новий баланс: {self.__balance}")
        else:
            print("[Помилка Bank] Сума поповнення має бути більшою за 0!")

    def withdraw(self, amount):
        if amount <= 0:
            print("[Помилка Bank] Сума зняття має бути більшою за 0!")
        elif amount > self.__balance:
            print("[Помилка Bank] Недостатньо коштів на рахунку!")
        else:
            self.__balance -= amount
            print(f"[Bank] Успішно знято {amount}. Залишок: {self.__balance}")

print("1) Перевірка BankAccount:")
account = BankAccount(100)
account.deposit(50)
account.withdraw(200)
account.withdraw(70)





class UserProfile:
    def __init__(self, email):
        self.__email = "placeholder@mail.com"
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" in value:
            self.__email = value
        else:
            print("[Помилка User] Некоректний формат email! Обов'язково має бути символ '@'.")

print("\n2) Перевірка UserProfile:")
user = UserProfile("invalid_email.com")
user.email = "alex@example.com"         
print(f"[Поточний email користувача {user.email}")




class Battery:
    def __init__(self, charge_level=100):
        self.__charge = 100
        self.charge = charge_level

    @property
    def charge(self):
        return self.__charge

    @charge.setter
    def charge(self, value):
        if 0 <= value <= 100:
            self.__charge = value
        else:
            print("[Помилка Battery] Заряд має бути в межах від 0 до 100%!")

print("\n3) Перевірка Battery:")
bat = Battery(85)
bat.charge = 150




class Speaker:
    def __init__(self, initial_volume=5):
        self.__volume = 5
        self.volume = initial_volume 

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        if 0 <= value <= 10:
            self.__volume = value
        else:
            print("[Помилка Speaker] Гучність має бути в діапазоні від 0 до 10!")

print("\n4) Перевірка Speaker:")
spk = Speaker(5)
spk.volume = 11




class Character:
    def __init__(self, name, initial_health=100):
        self.name = name
        self.__health = max(0, min(initial_health, 100))

    @property
    def health(self):
        return self.__health

    def damage(self, amount):
        if amount > 0:
            self.__health -= amount
            if self.__health < 0:
                self.__health = 0
            print(f"[Game] {self.name} отримав {amount} шкоди. Здоров'я: {self.__health}")
        else:
            print("[Помилка Game] Шкода має бути додатнім числом!")

    def heal(self, amount):
        if amount > 0:
            if self.__health == 0:
                print(f"[Game] {self.name} вже загинув, лікування неможливе!")
                return
            self.__health += amount
            if self.__health > 100:
                self.__health = 100
            print(f"[Game] {self.name} відновив {amount} здоров'я. Здоров'я: {self.__health}")
        else:
            print("[Помилка Game] Лікування має бути додатнім числом!")
print("\n5) Перевірка Character:")
hero = Character("Воїн", 100)
hero.damage(40)
hero.heal(20)
hero.damage(90)   
hero.heal(10)     




class PasswordManager:
    def __init__(self, initial_password):
        self.__password = "default_pass"  
        if len(initial_password) >= 8:
            self.__password = initial_password
        else:
            print("[PasswordManager] Початковий пароль занадто короткий! Встановлено пароль за замовчуванням.")

    def change_password(self, old, new):
        if old != self.__password:
            print("[Помилка PasswordManager] Старий пароль введено неправильно!")
        elif len(new) < 8:
            print("[Помилка PasswordManager] Новий пароль занадто короткий! Має бути ≥ 8 символів.")
        else:
            self.__password = new
            print("[PasswordManager] Пароль успішно змінено на новий.")

print("\n6) Перевірка PasswordManager:")
pm = PasswordManager("my_secret_123")
pm.change_password("wrong_old", "new_pass_123") 
pm.change_password("my_secret_123", "short")    
pm.change_password("my_secret_123", "valid_new_password") 
