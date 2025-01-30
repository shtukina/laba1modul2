account2 = BankAccount("", 50.0)  # Ожидается ошибка
except ValueError as e: print(f"Ошибка при создании банковского счёта: {e}")
try:
    account3 = BankAccount("1234567890", -10.0)  # Ожидается ошибка
except ValueError as e:
    print(f"Ошибка при создании банковского счёта: {e}")

try:
    account1.withdraw(200.0)  # Ожидается ошибка
except ValueError as e:
    print(f"Ошибка при снятии средств: {e}")

# Тестирование класса OnlineCourse
try:
    course1 = OnlineCourse("Python Programming", "John Doe", 10)
    print(f"Курс '{course1.title}' создан.")

    course2 = OnlineCourse("", "Jane Doe", 5)  # Ожидается ошибка
except ValueError as e: print(f"Ошибка при создании курса: {e}")

try:
    course3 = OnlineCourse("Data Science", "Alice Smith", -2)  # Ожидается ошибка
except ValueError as e: print(f"Ошибка при создании курса: {e}")

# Запуск тестов
test_classes()

