import gc


def experiment_cycle():
    print("=== Задание 4. Циклические ссылки и сборщик мусора ===")
    print(f"Автоматический сборщик мусора включен: {gc.isenabled()}")
    print(f"Пороги поколений сборщика: {gc.get_threshold()}")
    print(f"Статистика поколений: {gc.get_count()}")

    first = []
    second = []

    first.append(second)
    second.append(first)

    print("\nfirst ссылается на second:", first[0] is second)
    print("second ссылается на first:", second[0] is first)

    id_first, id_second = id(first), id(second)
    print(f"id(first)={id_first}, id(second)={id_second}")

    del first
    del second

    collected = gc.collect()
    print(f"Собрано недостижимых объектов через gc.collect(): {collected}\n")


def manual_gc_experiment():
    print("=== Дополнительный эксперимент с отключенным GC ===")
    gc.disable()
    try:
        for _ in range(5):
            a, b = [], []
            a.append(b)
            b.append(a)

        del a, b
        print("Циклы созданы и внешние ссылки удалены (GC отключен).")
        collected = gc.collect()
        print(f"Ручной сборщик мусора очистил объектов: {collected}")
    finally:
        gc.enable()
        print(f"Восстановлено состояние GC: isenabled()={gc.isenabled()}\n")


def practical_graph_task():
    print("=== Практическая задача: Модель графа ===")
    node_A = {"name": "A"}
    node_B = {"name": "B"}
    node_C = {"name": "C"}

    node_A["next"] = node_B
    node_B["next"] = node_C
    node_C["next"] = node_A

    node_D = {"name": "D", "next": None}

    print("Связи созданы: A -> B -> C -> A, D — независим.")

    del node_A, node_B, node_C

    collected = gc.collect()
    print(f"Число собранных объектов после удаления циклических узлов графа: {collected}")
    print(f"Независимый узел D доступен и сохранен: {node_D}")


if __name__ == "__main__":
    experiment_cycle()
    manual_gc_experiment()
    practical_graph_task()