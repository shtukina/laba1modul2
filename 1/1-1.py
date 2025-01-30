import datetime


class Dog:
    """Представляет собаку."""

    def __init__(self, name: str, breed: str, age: int):
        """Инициализирует объект класса Dog.

        Args:
            name (str): Имя собаки. Не может быть пустым.
            breed (str): Порода собаки.
            age (int): Возраст собаки. Должен быть неотрицательным.

        Raises:
            ValueError: Если имя пустое или возраст отрицательный.
        """
        if not name:
            raise ValueError("Имя собаки не может быть пустым.")
        if age < 0:
            raise ValueError("Возраст собаки не может быть отрицательным.")
        self.name: str = name
        self.breed: str = breed
        self.age: int = age

    def bark(self) -> str:
        """Заставляет собаку лаять."""
        return "Woof!"

    def celebrate_birthday(self) -> int:
        """Увеличивает возраст собаки на один год."""
        self.age += 1
        return self.age


class BankAccount:
    """Представляет банковский счёт."""

    def __init__(self, account_number: str, balance: float = 0.0):
        """Инициализирует объект класса BankAccount.

        Args:
            account_number (str): Номер счёта. Не может быть пустым.
            balance (float, optional): Начальный баланс. По умолчанию 0.0. Должен быть неотрицательным.

        Raises:
            ValueError: Если номер счёта пустой или баланс отрицательный.
        """
        if not account_number:
            raise ValueError("Номер счёта не может быть пустым.")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self.account_number: str = account_number
        self.balance: float = balance
        self.creation_date: datetime.date = datetime.date.today()

    def deposit(self, amount: float) -> float:
        """Вносит деньги на счёт."""
        if amount <= 0:
            raise ValueError("Сумма для внесения должна быть положительной.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Снимает деньги со счёта."""
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной.")
        if amount > self.balance:
            raise ValueError("Сумма для снятия превышает баланс.")
        self.balance -= amount
        return self.balance


class OnlineCourse:
    """Представляет онлайн-курс."""

    def __init__(self, title: str, instructor: str, duration_weeks: int):
        """Инициализирует объект класса OnlineCourse.

        Args:
            title (str): Название курса. Не может быть пустым.
            instructor (str): Имя преподавателя.
            duration_weeks (int): Продолжительность курса в неделях. Должна быть положительной.

        Raises:
            ValueError: Если название курса пустое или продолжительность отрицательная.
        """
        if not title:
            raise ValueError("Название курса не может быть пустым.")
        if duration_weeks <= 0:
            raise ValueError("Продолжительность курса должна быть положительной.")

        self.title: str = title
        self.instructor: str = instructor
        self.duration_weeks: int = duration_weeks


# Проверка работоспособности классов
def test_classes():
    # Тестирование класса Dog
    try:
        dog1 = Dog("Buddy", "Golden Retriever", 3)
        print(dog1.bark())  # Ожидается 'Woof!'

        dog2 = Dog("", "Labrador", 2)  # Ожидается ошибка
    except ValueError as e:
        print(f"Ошибка при создании собаки: {e}")

    try:
        dog3 = Dog("Max", "Beagle", -1)  # Ожидается ошибка
    except ValueError as e:
        print(f"Ошибка при создании собаки: {e}")
        
