#Підключаємо модуль для роботи з RegEx.
import re
from typing import Callable

def generator_numbers(text: str):
    #Шаблон цілого або дробового числа з необов'язковим знаком
    pattern = r"[+-]?\d+(\.\d+)?"

    #Розділяємо текст за пробілами та перевіряємо кожну частину за допомогою функції з підключеного модуля
    for word in text.split():
        if re.fullmatch(pattern, word):
            yield float(word)

def sum_profit(text: str, func: Callable) -> float:
    total = 0.0

    #Викликаємо передану функцію та підсумовуємо видані числа
    for number in func(text):
        total += number

    return total

text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими "
    "надходженнями 27.45 і 324.00 доларів."
)

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")