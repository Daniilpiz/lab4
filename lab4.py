import random
from typing import List, Optional, Tuple

class TreeNode:
    """Узел бинарного дерева поиска."""
    def __init__(self, value: int):
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

def insert(root: Optional[TreeNode], value: int) -> TreeNode:
    """Вставляет значение в бинарное дерево (допускаются дубликаты)."""
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:  # Дубликаты идут в правое поддерево
        root.right = insert(root.right, value)
    return root

def in_order_traversal(root: Optional[TreeNode], result: List[int]) -> None:
    """In-order обход дерева (сортировка по возрастанию)."""
    if root is not None:
        in_order_traversal(root.left, result)
        result.append(root.value)
        in_order_traversal(root.right, result)

def search_all_occurrences(root: Optional[TreeNode], value: int, level: int = 0) -> List[Tuple[bool, int]]:
   
    if root is None:
        return []
    
    results = []
    
    # Если нашли совпадение - добавляем в результаты
    if root.value == value:
        results.append((True, level))
    
    # Поиск в левом поддереве (только если значение МЕНЬШЕ или РАВНО)
    # Для дубликатов тоже ищем слева, если это нужно
    if value <= root.value:
        results.extend(search_all_occurrences(root.left, value, level + 1))
    
    # Поиск в правом поддереве (только если значение БОЛЬШЕ или РАВНО)
    if value >= root.value:
        results.extend(search_all_occurrences(root.right, value, level + 1))
    
    return results

def search_first_occurrence(root: Optional[TreeNode], value: int, level: int = 0) -> Tuple[bool, int]:
    if root is None:
        return False, -1
    
    if root.value == value:
        return True, level
    
    # Если значение меньше - ищем только слева
    if value < root.value:
        return search_first_occurrence(root.left, value, level + 1)
    
    # Если значение больше или равно - ищем только справа
    return search_first_occurrence(root.right, value, level + 1)

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
            search_value = int(input("\nВведите значение для поиска (или нечисло для выхода): "))
            
            # Поиск всех вхождений
            all_occurrences = search_all_occurrences(root, search_value)
            count = count_occurrences(root, search_value)
            
            if all_occurrences:
                print(f"Значение {search_value} найдено {count} раз(а)!")
                print("Уровни нахождения элементов:")
                for i, (found, level) in enumerate(all_occurrences, 1):
                    print(f"  Вхождение {i}: уровень {level}")
                
                # Первое вхождение
                first_found, first_level = search_first_occurrence(root, search_value)
                print(f"Первое вхождение: уровень {first_level}")
            else:
                print(f"Значение {search_value} не найдено")
            
        except ValueError:
            break
    
    print("\nПрограмма завершена")

if __name__ == "__main__":
    main()