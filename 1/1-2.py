from task import Car, Book, Tree  # Импортируем классы из предыдущего задания

if __name__ == "__main__":
    # Инстанцируем объекты классов
    car = Car("Toyota", "Camry", 2015)
    book = Book("1984", "George Orwell", 328)
    tree = Tree("Oak", 5.0)

    # Проверка метода start_engine с некорректными аргументами
    try:
        print(car.start_engine(123))  # Некорректный вызов с числом вместо строки
    except TypeError:
        print('Ошибка: неправильные данные')

    # Проверка метода read с некорректными аргументами
    try:
        print(book.read("ten"))  # Некорректный вызов с строкой вместо числа
    except TypeError:
        print('Ошибка: неправильные данные')

    # Проверка метода grow с некорректными аргументами
    try:
        print(tree.grow("three"))  # Некорректный вызов со строкой вместо числа
    except TypeError:
        print('Ошибка: неправильные данные')
