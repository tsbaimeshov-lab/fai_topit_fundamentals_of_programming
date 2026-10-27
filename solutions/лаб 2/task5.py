import sys
import tracemalloc


def part1_sizes():
    print("=== Часть 1. Размеры отдельных объектов ===")
    print(f"Размер empty list  : {sys.getsizeof([])} байт")
    print(f"Размер list из 10 int: {sys.getsizeof([i for i in range(10)])} байт")
    print(f"Размер tuple из 10 int: {sys.getsizeof(tuple(range(10)))} байт")
    print(f"Размер str из 10 символов: {sys.getsizeof('abcdefghij')} байт")
    print(f"Размер int (10)     : {sys.getsizeof(10)} байт")
    print(f"Размер None         : {sys.getsizeof(None)} байт\n")


def part2_growth():
    print("=== Часть 2. Рост списка (перевыделение памяти) ===")
    lst = []
    last_size = sys.getsizeof(lst)
    print(f"Начальный размер пустого списка: {last_size} байт")

    for i in range(100):
        lst.append(i)
        current_size = sys.getsizeof(lst)
        if current_size != last_size:
            print(f"Длина: {len(lst):3d} | Новый размер: {current_size:4d} байт (прирост {current_size - last_size} б)")
            last_size = current_size
    print()


def part3_tracemalloc():
    print("=== Часть 3. Измерение через tracemalloc ===")

    tracemalloc.start()
    numbers_list = list(range(100_000))
    current_list, peak_list = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tracemalloc.start()
    numbers_range = range(100_000)
    current_range, peak_range = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"list(range(100_000)) -> Текущая: {current_list / 1024:.2f} KB | Пиковая: {peak_list / 1024:.2f} KB")
    print(f"range(100_000)       -> Текущая: {current_range / 1024:.2f} KB | Пиковая: {peak_range / 1024:.2f} KB")
    print(f"Отношение пикового объема (list / range): {peak_list / max(peak_range, 1):.1f}x\n")


if __name__ == "__main__":
    part1_sizes()
    part2_growth()
    part3_tracemalloc()