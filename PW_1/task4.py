# варіант 3

class Library: # оголошення класу
    def __init__(self): # створення конструктору
        self.books = [] # створення масиву для зберігання даних

    def add_book(self, title): # метод додавання книги
        self.books.append(title) # використовуємо метод списку для додавання книги
        print(f"Книгу {title} додано")

    def remove_book(self, title): # метод видалення книги
        if title in self.books: # пошук книги
            self.books.remove(title) # видалення книги з списку
            print(f"Книгу {title} видалено")
        else: # повідомлення, якщо такої книги немає
            print(f"Книгу {title} не знайдено")

    def display_books(self): # метод відображення книжок
        if not self.books: # перевірка на заповнення
            print("Книготека порожня")
        else: # виведення книг
            for book in self.books:
                print(book)

my_library = Library() # створення об'єкта

my_library.add_book("book1")
my_library.add_book("book2")
my_library.add_book("book3")

my_library.display_books()

my_library.remove_book("book2")

my_library.display_books()

my_library.remove_book("book1111")

print("------------------")

my_library.remove_book("book1")
my_library.remove_book("book3")

my_library.display_books()