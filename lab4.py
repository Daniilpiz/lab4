import csv
import random
import time
from typing import List, Optional
from pathlib import Path

class TreeNode:
    """Узел бинарного дерева поиска."""
    def __init__(self, value: int):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

def insert(root: Optional[TreeNode], value: int) -> TreeNode:
    """Вставляет значение в бинарное дерево."""
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def in_order_traversal(root: Optional[TreeNode], result: List[int]) -> None:
    """In-order обход дерева (сортировка по возрастанию)."""
    if root is not None:
        in_order_traversal(root.left, result)
        result.append(root.value)
        in_order_traversal(root.right, result)

def generate_random_numbers(filename: str, count: int, min_val: int, max_val: int) -> List[int]:
    """Генерирует случайные числа и сохраняет в CSV."""
    numbers = [random.randint(min_val, max_val) for _ in range(count)]
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(numbers)
    return numbers

def manual_input(filename: str) -> List[int]:
    """Ручной ввод чисел."""
    print("Введите числа через пробел:")
    numbers = input().split()
    try:
        numbers = [int(num) for num in numbers]
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(numbers)
        return numbers
    except ValueError:
        print("Ошибка: введите только целые числа!")
        return manual_input(filename)

def get_fill_method() -> str:
    """Получает метод заполнения от пользователя."""
    print("Выберите способ заполнения файла:")
    print("1 - Вручную")
    print("2 - Случайными числами")
    while True:
        choice = input("Ваш выбор (1/2): ")
        if choice in ['1', '2']:
            return choice
        print("Неверный ввод! Попробуйте снова.")

# def fill_csv(filename: str) -> None:
#     """Заполняет CSV файл данными."""
#     choice = get_fill_method()
#     if choice == '1':
#         manual_input(filename)
#     else:
#         count = int(input("Введите количество чисел в массиве: "))
#         min_val = int(input("Введите нижнюю границу диапазона: "))
#         max_val = int(input("Введите верхнюю границу диапазона: "))
#         generate_random_numbers(filename, count, min_val, max_val)


def main():
    """Основная функция программы."""
    # Ввод и чтение данны
    n = int(input())
    data = [0]*n

    for i in range(n):
        data[i] = random.randint(-100, 100)


    # Сортировка с замером времени
    start_time = time.perf_counter()
    root = None
    for num in data:
        root = insert(root, num)
    
    sorted_data = []
    in_order_traversal(root, sorted_data)
    sort_time = time.perf_counter() - start_time

    

    print(sorted_data)
    print(f"\nСортировка завершена за {sort_time:.6f} секунд")

    # Предложение запустить бенчмарк
   

if __name__ == "__main__":
    main()