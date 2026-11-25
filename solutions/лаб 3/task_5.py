"""Лабораторная работа № 3. Задание 5: интеграционный анализатор успеваемости."""

from typing import Any


def mean(values: list[int | float]) -> float | None:
    """Вычисляет среднее арифметическое без использования встроенной sum()."""
    if not values:
        return None
    total = 0.0
    for item in values:
        total += item
    return total / len(values)


def minimum(values: list[int | float]) -> int | float | None:
    """Находит минимальный элемент без использования встроенной min()."""
    if not values:
        return None
    current_min = values[0]
    for item in values[1:]:
        if item < current_min:
            current_min = item
    return current_min


def maximum(values: list[int | float]) -> int | float | None:
    """Находит максимальный элемент без использования встроенной max()."""
    if not values:
        return None
    current_max = values[0]
    for item in values[1:]:
        if item > current_max:
            current_max = item
    return current_max


def classify(score: float | None) -> str:
    """Определяет категорию успеваемости по среднему баллу."""
    if score is None:
        return "нет данных"
    if score >= 90:
        return "отличный"
    if score >= 75:
        return "хороший"
    if score >= 60:
        return "удовлетворительный"
    return "недостаточный"


def student_summary(name: str, results: list[int]) -> dict[str, Any]:
    """Формирует индивидуальную сводку по одному студенту."""
    avg = mean(results)
    return {
        "name": name,
        "count": len(results),
        "mean": avg,
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(avg),
    }


def find_top_students(students: dict[str, list[int]]) -> list[str]:
    """Возвращает список имен всех студентов с максимальным средним баллом."""
    best_mean: float | None = None
    leaders: list[str] = []

    for name, results in students.items():
        avg = mean(results)
        if avg is None:
            continue
        if best_mean is None or avg > best_mean:
            best_mean = avg
            leaders = [name]
        elif avg == best_mean:
            leaders.append(name)

    return leaders


def group_summary(students: dict[str, list[int]]) -> dict[str, Any]:
    """Вычисляет агрегированную статистику по всей группе без изменения students."""
    summaries = [student_summary(name, results) for name, results in students.items()]
    valid_means = [item["mean"] for item in summaries if item["mean"] is not None]

    category_counts: dict[str, int] = {}
    for item in summaries:
        cat = item["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1

    ranking = sorted(
        (item for item in summaries if item["mean"] is not None),
        key=lambda item: (-item["mean"], item["name"]),
    )

    return {
        "total_students": len(students),
        "evaluated_students": len(valid_means),
        "group_mean": mean(valid_means),
        "category_counts": category_counts,
        "top_students": find_top_students(students),
        "ranking": ranking,
    }


def format_report(student_data: list[dict[str, Any]], group_data: dict[str, Any]) -> str:
    """Форматирует многострочный текстовый отчет по студентам и группе."""
    if not student_data:
        return "Отчет по группе: данные о студентах отсутствуют."

    lines = [
        "=== ОТЧЕТ ПО УСПЕВАЕМОСТИ ГРУППЫ ===",
        f"{'Студент':<12} | {'Работ':>5} | {'Средний':>7} | {'Мин':>4} | {'Макс':>4} | Категория",
        "-" * 68,
    ]

    for item in student_data:
        mean_str = f"{item['mean']:.2f}" if item["mean"] is not None else "—"
        min_str = str(item["min"]) if item["min"] is not None else "—"
        max_str = str(item["max"]) if item["max"] is not None else "—"
        lines.append(
            f"{item['name']:<12} | {item['count']:>5} | {mean_str:>7} | "
            f"{min_str:>4} | {max_str:>4} | {item['category']}"
        )

    group_mean_str = (
        f"{group_data['group_mean']:.2f}"
        if group_data["group_mean"] is not None
        else "—"
    )
    leaders_str = ", ".join(group_data["top_students"]) or "—"

    lines.extend(
        [
            "-" * 68,
            f"Всего студентов: {group_data['total_students']} "
            f"(с оценками: {group_data['evaluated_students']})",
            f"Средний балл группы: {group_mean_str}",
            f"Лидеры группы: {leaders_str}",
            "Распределение по категориям:",
        ]
    )

    for category, count in group_data["category_counts"].items():
        lines.append(f"  - {category}: {count}")

    if group_data["ranking"]:
        lines.append("Рейтинг студентов:")
        for place, item in enumerate(group_data["ranking"], start=1):
            lines.append(f"  {place}. {item['name']} — {item['mean']:.2f}")

    return "\n".join(lines)


def run_tests() -> None:
    """Проверяет все 6 тестовых сценариев из отчета."""
    # Сценарий 1: обычный набор данных (4 студента, все 4 категории)
    group_1 = {
        "Анна": [80, 85, 85],          # 83.33 -> хороший
        "Борис": [68, 70, 72],         # 70.00 -> удовлетворительный
        "Дарья": [90, 95, 92, 98],     # 93.75 -> отличный
        "Илья": [54, 58, 55, 59, 57],  # 56.60 -> недостаточный
    }
    summary_1 = group_summary(group_1)
    assert summary_1["top_students"] == ["Дарья"]
    assert round(summary_1["group_mean"], 2) == 75.92
    assert summary_1["category_counts"] == {
        "хороший": 1,
        "удовлетворительный": 1,
        "отличный": 1,
        "недостаточный": 1,
    }

    # Сценарий 2: один студент
    group_2 = {"Анна": [80, 90]}
    summary_2 = group_summary(group_2)
    assert summary_2["top_students"] == ["Анна"]
    assert summary_2["group_mean"] == 85.0
    assert summary_2["category_counts"] == {"хороший": 1}

    # Сценарий 3: несколько лидеров
    group_3 = {"Анна": [90, 90], "Дарья": [85, 95]}
    assert find_top_students(group_3) == ["Анна", "Дарья"]

    # Сценарий 4: пустая группа
    summary_4 = group_summary({})
    assert summary_4["top_students"] == []
    assert summary_4["group_mean"] is None
    assert summary_4["category_counts"] == {}
    assert "отсутствуют" in format_report([], summary_4)

    # Сценарий 5: студент без результатов
    group_5 = {"Анна": [80], "Илья": []}
    ilya = student_summary("Илья", [])
    assert ilya["mean"] is None and ilya["min"] is None and ilya["max"] is None
    assert ilya["category"] == "нет данных"
    summary_5 = group_summary(group_5)
    assert summary_5["group_mean"] == 80.0
    assert summary_5["evaluated_students"] == 1

    # Сценарий 6: граничные значения
    boundary_expected = [
        (59, "недостаточный"),
        (60, "удовлетворительный"),
        (74, "удовлетворительный"),
        (75, "хороший"),
        (89, "хороший"),
        (90, "отличный"),
    ]
    for score, expected_cat in boundary_expected:
        assert classify(float(score)) == expected_cat


def main() -> None:
    run_tests()
    students = {
        "Анна": [80, 85, 85],
        "Борис": [68, 70, 72],
        "Дарья": [90, 95, 92, 98],
        "Илья": [54, 58, 55, 59, 57],
    }
    student_data = [student_summary(name, scores) for name, scores in students.items()]
    group_data = group_summary(students)
    print(format_report(student_data, group_data))


if __name__ == "__main__":
    main()