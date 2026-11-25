Attempt = tuple[str, str, int]


def build_indexes(
    log: list[Attempt],
) -> tuple[
    set[str],
    set[str],
    dict[str, list[tuple[str, int]]],
    dict[tuple[str, str], int],
    dict[tuple[str, str], int],
]:
    """Строит множества и словари для быстрого анализа журнала попыток."""
    students: set[str] = set()
    labs: set[str] = set()
    by_student: dict[str, list[tuple[str, int]]] = {}
    best_scores: dict[tuple[str, str], int] = {}
    attempt_counts: dict[tuple[str, str], int] = {}

    for student, lab, score in log:
        students.add(student)
        labs.add(lab)

        by_student.setdefault(student, []).append((lab, score))

        key = (student, lab)
        attempt_counts[key] = attempt_counts.get(key, 0) + 1
        if key not in best_scores or score > best_scores[key]:
            best_scores[key] = score

    return students, labs, by_student, best_scores, attempt_counts


def students_with_both_labs(
    log: list[Attempt], lab_a: str, lab_b: str
) -> set[str]:
    """Возвращает множество студентов, сдавших обе указанные лабораторные работы."""
    completed_a = {student for student, lab, _ in log if lab == lab_a}
    completed_b = {student for student, lab, _ in log if lab == lab_b}
    return completed_a & completed_b


def handle_query(
    query: str,
    best_scores: dict[tuple[str, str], int],
    attempt_counts: dict[tuple[str, str], int],
) -> str:
    """Обрабатывает текстовые запросы вида 'best Анна lab_1' или 'attempts Анна lab_1'."""
    parts = query.strip().split()
    if len(parts) != 3:
        return "Ошибка формата запроса. Ожидается: <best|attempts> <студент> <работа>"

    command, student, lab = parts
    key = (student, lab)

    match command:
        case "best":
            if key in best_scores:
                return f"Лучший балл ({student}, {lab}): {best_scores[key]}"
            return f"Записей для ({student}, {lab}) не найдено"
        case "attempts":
            return f"Число попыток ({student}, {lab}): {attempt_counts.get(key, 0)}"
        case _:
            return f"Неизвестная команда: {command}"


def demonstrate_unhashable_list() -> str:
    """Показывает, почему list нельзя использовать как ключ словаря."""
    try:
        invalid_dict = {["Анна", "lab_1"]: 90}  # type: ignore[unhashable-type]
        return str(invalid_dict)
    except TypeError as err:
        return f"Ожидаемая ошибка при использовании list как ключа: {err}"


def run_tests() -> None:
    """Проверяет корректность индексации, пересечения множеств и обработки запросов."""
    sample_log: list[Attempt] = [
        ("Анна", "lab_1", 78),
        ("Анна", "lab_1", 92),
        ("Анна", "lab_2", 85),
        ("Борис", "lab_1", 70),
        ("Дарья", "lab_1", 95),
        ("Дарья", "lab_2", 98),
        ("Илья", "lab_2", 64),
    ]

    students, labs, by_student, best_scores, attempt_counts = build_indexes(sample_log)

    assert students == {"Анна", "Борис", "Дарья", "Илья"}
    assert labs == {"lab_1", "lab_2"}
    assert len(by_student["Анна"]) == 3
    assert best_scores[("Анна", "lab_1")] == 92
    assert attempt_counts[("Анна", "lab_1")] == 2
    assert students_with_both_labs(sample_log, "lab_1", "lab_2") == {"Анна", "Дарья"}

    assert handle_query("best Анна lab_1", best_scores, attempt_counts).endswith("92")
    assert handle_query("attempts Анна lab_1", best_scores, attempt_counts).endswith("2")
    assert "не найдено" in handle_query("best Илья lab_1", best_scores, attempt_counts)


def main() -> None:
    run_tests()
    sample_log: list[Attempt] = [
        ("Анна", "lab_1", 78),
        ("Анна", "lab_1", 92),
        ("Анна", "lab_2", 85),
        ("Борис", "lab_1", 70),
        ("Дарья", "lab_1", 95),
        ("Дарья", "lab_2", 98),
        ("Илья", "lab_2", 64),
    ]
    students, labs, _, best_scores, attempt_counts = build_indexes(sample_log)

    print("Задание 3: все проверки коллекций пройдены.")
    print(f"Уникальные студенты: {sorted(students)}")
    print(f"Уникальные работы: {sorted(labs)}")
    print(f"Сдали lab_1 и lab_2: {sorted(students_with_both_labs(sample_log, 'lab_1', 'lab_2'))}")
    print(handle_query("best Анна lab_1", best_scores, attempt_counts))
    print(handle_query("attempts Анна lab_1", best_scores, attempt_counts))
    print(demonstrate_unhashable_list())


if __name__ == "__main__":
    main()