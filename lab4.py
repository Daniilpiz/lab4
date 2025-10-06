import random
import time
from typing import List, Optional

class TreeNode:
    """Узел бинарного дерева поиска."""
    def __init__(self, value: int):
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

def insert(root: Optional[TreeNode], value: int) -> TreeNode:
    """Вставляет уникальное значение в бинарное дерево."""
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:  # Изменено условие для исключения дубликатов
        root.right = insert(root.right, value)
    return root

def in_order_traversal(root: Optional[TreeNode], result: List[int]) -> None:
    """In-order обход дерева (сортировка по возрастанию)."""
    if root is not None:
        in_order_traversal(root.left, result)
        result.append(root.value)
        in_order_traversal(root.right, result)

def search(root: Optional[TreeNode], value: int) -> bool:
    """Поиск значения в бинарном дереве."""
    if root is None:
        return False
    if root.value == value:
        return True
    elif value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)

def count_occurrences(root: Optional[TreeNode], value: int) -> int:
    """Подсчёт числа вхождений заданного элемента в дерево."""
    if root is None:
        return 0
    count = 0
    if root.value == value:
        count += 1
    count += count_occurrences(root.left, value)
    count += count_occurrences(root.right, value)
    return count

def generate_random_numbers(count: int, min_val: int, max_val: int) -> List[int]:
    """Генерирует случайные числа."""
    return [random.randint(min_val, max_val) for _ in range(count)]

def manual_input() -> List[int]:
    """Ручной ввод чисел."""
    while True:
        try:
            print("Введите числа через пробел:")
            numbers = input().split()
            numbers = [int(num) for num in numbers]
            return numbers
        except ValueError:
            print("Ошибка: введите только целые числа!")

def get_fill_method() -> str:
    """Получает метод заполнения от пользователя."""
    print("Выберите способ заполнения:")
    print("1 - Вручную")
    print("2 - Случайными числами")
    while True:
        choice = input("Ваш выбор (1/2): ")
        if choice in ['1', '2']:
            return choice
        print("Неверный ввод! Попробуйте снова.")

def fill_data() -> List[int]:
    """Заполняет данные."""
    choice = get_fill_method()
    if choice == '1':
        return manual_input()
    else:
        while True:
            try:
                count = int(input("Введите количество чисел в массиве: "))
                min_val = int(input("Введите нижнюю границу диапазона: "))
                max_val = int(input("Введите верхнюю границу диапазона: "))
                return generate_random_numbers(count, min_val, max_val)
            except ValueError:
                print("Ошибка: введите целые числа!")

def benchmark_sorting(data: List[int]) -> float:
    """Замеряет время сортировки."""
    start_time = time.perf_counter()
    root = None
    for num in data:
        root = insert(root, num)
    
    sorted_data = []
    in_order_traversal(root, sorted_data)
    sort_time = time.perf_counter() - start_time
    return sort_time, sorted_data

def print_tree(root: Optional[TreeNode], level: int = 0, prefix: str = ""):
    """Рекурсивно печатает дерево в консоль."""
    if root is not None:
        # Печатаем правое поддерево
        print_tree(root.right, level + 1, "    " + "┌─── ")
        
        # Печатаем текущий узел
        print("    " * level + prefix + str(root.value))
        
        # Печатаем левое поддерево
        print_tree(root.left, level + 1, "    " + "└─── ")

def main():
    """Основная функция программы."""
    print("\n--- Создание бинарного дерева поиска ---\n")
    
    # Выбор способа заполнения
    data = fill_data()
    print(f"\nИсходные данные: {data}\n")
    
    # Создание дерева
    root = None
    print("--- Процесс создания дерева ---")
    for num in data:
        root = insert(root, num)
        print(f"Добавлено значение: {num}")
    
    # Визуализация дерева
    print("\n--- Визуализация дерева ---")
    print_tree(root)
    
    # Демонстрация поиска
    while True:
        try:
            search_value = int(input("\nВведите значение для поиска (или 0 для выхода): "))
            if search_value == 0:
                break
            
            if search(root, search_value):
                count = count_occurrences(root, search_value)
                print(f"Значение {search_value} найдено! Количество вхождений: {count}")
            else:
                print(f"Значение {search_value} не найдено")
            
        except ValueError:
            print("Ошибка: введите целое число!")
    
    print("\nПрограмма завершена")

if __name__ == "__main__":
    main()