import json
import os
from datetime import datetime

FILENAME = "library.json"

class Book:
    def __init__(self, book_id, title, author, year, is_borrowed=False):
        self.id = int(book_id)
        self.title = title
        self.author = author
        self.year = int(year)
        self.is_borrowed = is_borrowed

    def print_info(self):
        status = "📕 [видана]" if self.is_borrowed else "📗 [у бібліотеці]"
        print(f"ID: {self.id} | {status} | «{self.title}» — {self.author} ({self.year} р.)")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "is_borrowed": self.is_borrowed
        }


class Library:
    def __init__(self):
        self.books = []
        self.load()

    def load(self):
        if not os.path.exists(FILENAME):
            self.books = []
            return
        try:
            with open(FILENAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [
                    Book(b["id"], b["title"], b["author"], b["year"], b["is_borrowed"]) 
                    for b in data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []
        except Exception as e:
            print(f"❌ Помилка завантаження даних: {e}")
            self.books = []

    def save(self):
        try:
            with open(FILENAME, "w", encoding="utf-8") as file:
                json.dump([b.to_dict() for b in self.books], file, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"❌ Помилка збереження даних: {e}")

    def get_next_id(self):
        if not self.books:
            return 1
        return max(b.id for b in self.books) + 1

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def input_year(self):
        current_year = datetime.now().year
        while True:
            try:
                year_input = input("⏳ Введіть рік видання (від 1500): ").strip()
                year = int(year_input)
                if 1500 <= year <= current_year:
                    return year
                print(f"❌ Рік має бути в діапазоні від 1500 до {current_year}.")
            except ValueError:
                print("❌ Будь ласка, введіть коректне числове значення року.")

    def input_id(self, prompt):
        while True:
            try:
                id_input = input(prompt).strip()
                return int(id_input)
            except ValueError:
                print("❌ ID має бути цілим числом. Спробуйте знову.")

    def add_book_menu(self):
        print("\n--- 📝 Додавання книги ---")
        title = input("📖 Введіть назву книги: ").strip()
        author = input("✍️ Введіть автора книги: ").strip()
        
        if not title or not author:
            print("❌ Назва та автор не можуть бути порожніми!")
            return
            
        year = self.input_year()
        new_id = self.get_next_id()
        
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save()
        print(f"✅ Книгу «{title}» успішно додано під ID: {new_id}!")

    def view_all_books_menu(self):
        print("\n--- 📚 Перегляд усіх книг ---")
        if not self.books:
            print("📭 Бібліотека порожня. Немає жодної книги.")
            return

        print("Оберіть критерій сортування:")
        print("1. За назвою")
        print("2. За автором")
        choice = input("Ваш вибір (1-2): ").strip()

        if choice == "2":
            sorted_books = sorted(self.books, key=lambda b: b.author.lower())
            print("\n📋 Список книг (відсортовано за автором):")
        else:
            sorted_books = sorted(self.books, key=lambda b: b.title.lower())
            print("\n📋 Список книг (відсортовано за назвою):")

        for book in sorted_books:
            book.print_info()

    def delete_book_menu(self):
        print("\n--- 🗑️ Видалення книги ---")
        book_id = self.input_id("🔢 Введіть ID книги для видалення: ")
        book = self.find_book_by_id(book_id)

        if book:
            self.books.remove(book)
            self.save()
            print(f"✅ Книгу «{book.title}» (ID: {book_id}) успішно видалено.")
        else:
            print("❌ Книгу з таким ID не знайдено.")

    def borrow_book_menu(self):
        print("\n--- 🤝 Видати книгу читачеві ---")
        book_id = self.input_id("🔢 Введіть ID книги для видачі: ")
        book = self.find_book_by_id(book_id)

        if not book:
            print("❌ Книгу з таким ID не знайдено.")
        elif book.is_borrowed:
            print(f"❌ Книга «{book.title}» вже видана іншому читачеві!")
        else:
            book.is_borrowed = True
            self.save()
            print(f"✅ Книгу «{book.title}» успішно видано читачеві! 📕")

    def return_book_menu(self):
        print("\n--- ↩️ Повернути книгу ---")
        book_id = self.input_id("🔢 Введіть ID книги для повернення: ")
        book = self.find_book_by_id(book_id)

        if not book:
            print("❌ Книгу з таким ID не знайдено.")
        elif not book.is_borrowed:
            print(f"⚠️ Книга «{book.title}» вже перебуває у бібліотеці! 📗")
        else:
            book.is_borrowed = False
            self.save()
            print(f"✅ Книгу «{book.title}» успішно повернуто до бібліотеки! 📗")

    def find_by_author_menu(self):
        print("\n--- 🔍 Пошук за автором ---")
        author_query = input("✍️ Введіть ім'я або прізвище автора: ").strip().lower()
        
        found_books = [b for b in self.books if author_query in b.author.lower()]
        
        if found_books:
            print(f"\n🎯 Знайдені книги автора ({len(found_books)}):")
            for book in found_books:
                book.print_info()
        else:
            print("❌ Книг цього автора не знайдено.")

    def find_by_keyword_menu(self):
        print("\n--- 🔍 Пошук за ключовим словом у назві ---")
        keyword = input("🔤 Введіть підрядок для пошуку в назві: ").strip().lower()
        
        found_books = [b for b in self.books if keyword in b.title.lower()]
        
        if found_books:
            print(f"\n🎯 Знайдені книги за ключовим словом ({len(found_books)}):")
            for book in found_books:
                book.print_info()
        else:
            print("❌ Жодної книги з таким ключовим словом не знайдено.")


def main():
    library = Library()

    while True:
        print("\n--- Бібліотека ---")
        print("1. Додати книгу")
        print("2. Переглянути всі книги")
        print("3. Видалити книгу")
        print("4. Видати книгу")
        print("5. Повернути книгу")
        print("6. Пошук за автором")
        print("7. Пошук за ключовим словом")
        print("8. Вийти")
        
        choice = input("👉 Виберіть пункт меню (1-8): ").strip()
        
        if choice == "1":
            library.add_book_menu()
        elif choice == "2":
            library.view_all_books_menu()
        elif choice == "3":
            library.delete_book_menu()
        elif choice == "4":
            library.borrow_book_menu()
        elif choice == "5":
            library.return_book_menu()
        elif choice == "6":
            library.find_by_author_menu()
        elif choice == "7":
            library.find_by_keyword_menu()
        elif choice == "8":
            print("\n👋 Дякуємо за використання бібліотеки! До побачення.")
            break
        else:
            print("❌ Неправильний вибір. Будь ласка, введіть число від 1 до 8.")


if __name__ == "__main__":
    main()
