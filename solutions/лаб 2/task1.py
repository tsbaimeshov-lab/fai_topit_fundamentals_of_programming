import copy


def experiment_a():
    print("=== Эксперимент A. Неизменяемый объект ===")
    a = 10
    b = a
    print(f"До изменения: a={a}, b={b}, id(a)={id(a)}, id(b)={id(b)}")

    a += 1
    print(f"После a += 1: a={a}, b={b}, id(a)={id(a)}, id(b)={id(b)}")
    print("Объяснение: int — неизменяемый тип. Операция a += 1 создает новый объект 11 в памяти и перенаправляет имя 'a' на него. 'b' продолжает ссылаться на 10.\n")


def experiment_b():
    print("=== Эксперимент B. Изменяемый объект ===")
    first = [10, 20]
    second = first
    print(f"До изменения: first={first}, second={second}")
    print(f"id(first)={id(first)}, id(second)={id(second)}")

    second.append(30)
    print(f"После second.append(30): first={first}, second={second}")
    print(f"id(first)={id(first)}, id(second)={id(second)}")

    # 1. Переназначение second
    second = [10, 20, 30]
    print(f"\nПосле переназначения second = [10, 20, 30]:")
    print(f"first={first}, id(first)={id(first)}")
    print(f"second={second}, id(second)={id(second)}")

    # 2. Сравнение
    print(f"first == second: {first == second} (значения равны)")
    print(f"first is second: {first is second} (объекты разные)")

    # 3. Изменение нового списка
    second.append(40)
    print(f"\nПосле second.append(40):")
    print(f"first={first} (не изменился)")
    print(f"second={second} (изменился)\n")


def practical_task():
    print("=== Практическая задача: Конфигурации проекта ===")
    # Связанная конфигурация (простая ссылка)
    config1 = {
        "name": "Project Alpha",
        "members": ["Alice", "Bob"],
        "params": {"debug": False, "timeout": 30}
    }
    config2_linked = config1

    # Нежелательное совместное изменение
    config2_linked["params"]["debug"] = True
    print("После нежелательного изменения через config2_linked:")
    print(f"config1 debug: {config1['params']['debug']} (ошибочно изменилось!)")

    # Действительно независимая конфигурация
    config1["params"]["debug"] = False  # сброс
    config2_independent = copy.deepcopy(config1)
    config2_independent["params"]["debug"] = True
    config2_independent["members"].append("Charlie")

    assert config1["params"] is not config2_independent["params"]
    assert config1["members"] is not config2_independent["members"]

    print("\nСостояние конфигураций после независимого изменения:")
    print(f"config1: {config1}")
    print(f"config2_independent: {config2_independent}")
    print("Итог: config1 и config2_independent полностью независимы в памяти.\n")


if __name__ == "__main__":
    experiment_a()
    experiment_b()
    practical_task()