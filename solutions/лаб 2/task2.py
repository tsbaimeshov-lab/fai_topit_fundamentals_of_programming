import copy


def main():
    print("=== Задание 2. Поверхностное и глубокое копирование ===")
    original = [
        ["Python", 5],
        ["Algorithms", 4],
    ]

    alias = original
    shallow = original.copy()
    deep = copy.deepcopy(original)

    def print_info(header):
        print(f"\n--- {header} ---")
        print(f"original: {original}")
        print(f"alias   : {alias}")
        print(f"shallow : {shallow}")
        print(f"deep    : {deep}")
        print("Внешние id:")
        print(f"  orig:{id(original)}, alias:{id(alias)}, shallow:{id(shallow)}, deep:{id(deep)}")
        print("id первого вложенного списка [Python, 5]:")
        print(f"  orig:{id(original[0])}, alias:{id(alias[0])}, shallow:{id(shallow[0])}, deep:{id(deep[0])}")
        print("id первой оценки (5):")
        print(f"  orig:{id(original[0][1])}, alias:{id(alias[0][1])}, shallow:{id(shallow[0][1])}, deep:{id(deep[0][1])}")

    print_info("Исходное состояние")

    # Шаг 1
    original.append(["Databases", 5])
    print_info("После original.append(['Databases', 5])")

    # Шаг 2
    original[0][1] = 3
    print_info("После original[0][1] = 3")

    # Исследование ошибочной матрицы
    print("\n--- Исследование создания матрицы ---")
    wrong_matrix = [[0] * 3] * 3
    wrong_matrix[0][0] = 1
    print(f"wrong_matrix после wrong_matrix[0][0] = 1:\n{wrong_matrix}")
    print(f"id строк wrong_matrix: {[id(row) for row in wrong_matrix]} (все строки — один объект!)")

    correct_matrix = [[0] * 3 for _ in range(3)]
    correct_matrix[0][0] = 1
    print(f"correct_matrix после correct_matrix[0][0] = 1:\n{correct_matrix}")
    print(f"id строк correct_matrix: {[id(row) for row in correct_matrix]} (каждая строка — уникальный объект)")


if __name__ == "__main__":
    main()