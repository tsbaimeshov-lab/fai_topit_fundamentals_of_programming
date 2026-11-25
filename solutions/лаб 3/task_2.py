def analyze_measurements(values: list[int]) -> dict[str, int | float]:
    if not values:
        raise ValueError("Список измерений не должен быть пустым.")

    total = 0
    min_val = values[0]
    max_val = values[0]
    even_count = 0

    for x in values:
        total += x
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
        if x % 2 == 0:
            even_count += 1

    average = total / len(values)
    above_avg_count = 0
    for x in values:
        if x > average:
            above_avg_count += 1

    return {
        "total": total,
        "average": average,
        "min": min_val,
        "max": max_val,
        "even_count": even_count,
        "above_avg_count": above_avg_count,
    }


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def linear_search(values: list[int], target: int) -> tuple[int, int]:
    comparisons = 0
    for index, item in enumerate(values):
        comparisons += 1
        if item == target:
            return index, comparisons
    return -1, comparisons


def selection_sort(values: list[int]) -> list[int]:
    result = list(values)
    n = len(result)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        if min_idx != i:
            result[i], result[min_idx] = result[min_idx], result[i]
    return result


def binary_search(sorted_values: list[int], target: int) -> tuple[int, int]:
    left = 0
    right = len(sorted_values) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if sorted_values[mid] == target:
            return mid, comparisons
        if sorted_values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons


def run_tests() -> None:
    stats = analyze_measurements([10, 15, 20, 25, 30])
    assert stats["total"] == 100
    assert stats["min"] == 10
    assert stats["max"] == 30
    assert stats["even_count"] == 3
    assert stats["above_avg_count"] == 2

    primes = [n for n in range(20) if is_prime(n)]
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19]
    assert not is_prime(1)
    assert not is_prime(9)
    assert is_prime(97)

    raw = [42, 7, 19, 3, 25, 7]
    ordered = selection_sort(raw)
    assert ordered == [3, 7, 7, 19, 25, 42]
    assert raw == [42, 7, 19, 3, 25, 7]

    idx_lin, cmp_lin = linear_search(ordered, 25)
    assert idx_lin == 4 and cmp_lin == 5

    idx_bin, cmp_bin = binary_search(ordered, 25)
    assert idx_bin == 4 and cmp_bin <= 3

    assert binary_search(ordered, 100)[0] == -1


def main() -> None:
    run_tests()
    print("Задание 2: все проверки алгоритмов пройдены.")
    print("\nСравнение числа сравнений в худшем случае (элемент отсутствует):")
    print(f"{'n':>6} | {'Линейный':>10} | {'Бинарный':>10} | {'Ускорение':>10}")
    print("-" * 45)
    for size in (10, 100, 1000):
        data = list(range(size))
        _, lin_cmp = linear_search(data, -1)
        _, bin_cmp = binary_search(data, -1)
        ratio = lin_cmp / bin_cmp
        print(f"{size:>6} | {lin_cmp:>10} | {bin_cmp:>10} | {ratio:>9.1f}x")


if __name__ == "__main__":
    main()