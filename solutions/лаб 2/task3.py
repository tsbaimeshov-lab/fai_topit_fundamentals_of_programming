import sys
import weakref


class Record:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Record({self.name})"


def experiment_refcount():
    print("=== Задание 3. Исследование счетчика ссылок ===")
    data = [1, 2, 3]
    print("После создания:", sys.getrefcount(data))

    alias = data
    print("После создания alias:", sys.getrefcount(data))

    container = [data]
    print("После помещения в контейнер:", sys.getrefcount(data))

    del alias
    print("После del alias:", sys.getrefcount(data))

    container.clear()
    print("После очистки контейнера:", sys.getrefcount(data))
    print()


def experiment_weakref():
    print("=== Эксперимент со слабой ссылкой ===")
    record = Record("Test")
    weak_record = weakref.ref(record)

    print("Слабая ссылка при живом объекте:", weak_record())
    del record
    print("Слабая ссылка после del record:", weak_record())
    print()


def practical_task():
    print("=== Практическая задача: WeakValueDictionary ===")
    registry = weakref.WeakValueDictionary()

    r1 = Record("Obj1")
    r2 = Record("Obj2")
    r3 = Record("Obj3")

    registry["r1"] = r1
    registry["r2"] = r2
    registry["r3"] = r3

    print("Реестр до удаления сильных ссылок:", list(registry.keys()))

    # Удаляем временную сильную ссылку на r3
    del r3
    print("Реестр после del r3:", list(registry.keys()))

    # Удаляем еще одну сильную ссылку
    del r1
    print("Реестр после del r1:", list(registry.keys()))


if __name__ == "__main__":
    experiment_refcount()
    experiment_weakref()
    practical_task()