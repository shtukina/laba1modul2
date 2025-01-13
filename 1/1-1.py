class Car:
    """
    Класс, описывающий автомобиль.

    Attributes:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int):
        if year < 1886 or year > 2023:  # Первой машины считается 1886 год
            raise ValueError("Год выпуска должен быть между 1886 и 2023.")
        self.brand = brand
        self.model = model
        self.year = year

    def get_age(self) -> int:
        """
        Возвращает возраст автомобиля.

        Returns:
            int: Возраст автомобиля в годах.

        >>> car = Car('Toyota', 'Camry', 2015)
        >>> car.get_age()
        8
        """
        return 2023 - self.year

    def start_engine(self) -> str:
        """
        Запускает двигатель автомобиля.

        Returns:
            str: Сообщение о запуске двигателя.

        >>> car = Car('Honda', 'Civic', 2020)
        >>> car.start_engine()
        'Двигатель Honda Civic запущен.'
        """
        return f'Двигатель {self.brand} {self.model} запущен.'


class Book:
    """
    Класс, описывающий книгу.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
        pages (int): Количество страниц в книге.
    """

    def __init__(self, title: str, author: str, pages: int):
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_read: int) -> str:
        """
        Читает указанное количество страниц из книги.

        Args:
            pages_read (int): Количество страниц для чтения.

        Returns:
            str: Сообщение о прочитанных страницах.

        Raises:
            ValueError: Если pages_read меньше или равно 0.

        >>> book = Book('1984', 'George Orwell', 328)
        >>> book.read(50)
        'Вы прочитали 50 страниц из книги "1984".'
        """
        if pages_read <= 0:
            raise ValueError("Количество прочитанных страниц должно быть положительным.")

        return f'Вы прочитали {pages_read} страниц из книги "{self.title}".'

    def get_info(self) -> str:
        """
        Возвращает информацию о книге.

        Returns:
            str: Информация о книге.

        >>> book = Book('The Great Gatsby', 'F. Scott Fitzgerald', 180)
        >>> book.get_info()
        'Книга "The Great Gatsby" написана F. Scott Fitzgerald и содержит 180 страниц.'
        """
        return f'Книга "{self.title}" написана {self.author} и содержит {self.pages} страниц.'


class Tree:
    """
    Класс, описывающий дерево.

    Attributes:
        species (str): Вид дерева.
        height (float): Высота дерева в метрах.
    """

    def __init__(self, species: str, height: float):
        if height < 0:
            raise ValueError("Высота дерева не может быть отрицательной.")
        self.species = species
        self.height = height

    def grow(self, increase: float = 1.0) -> None:
        """
        Увеличивает высоту дерева.

        Args:
            increase (float): Увеличение высоты дерева в метрах. По умолчанию 1.0.

        Raises:
            ValueError: Если increase отрицательное.

        >>> tree = Tree('Oak', 5.0)
        >>> tree.grow(2.0)
        >>> tree.height
        7.0
        """
        if increase < 0:
            raise ValueError("Увеличение высоты не может быть отрицательным.")

        self.height += increase

    def get_info(self) -> str:
        """
        Возвращает информацию о дереве.

        Returns:
            str: Информация о дереве.

        >>> tree = Tree('Pine', 10.0)
        >>> tree.get_info()
        'Дерево вида Pine имеет высоту 10.0 метров.'
        """
        return f'Дерево вида {self.species} имеет высоту {self.height} метров.'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
