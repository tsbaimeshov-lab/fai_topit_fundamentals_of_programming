LEVELS = (
    "недостаточный",
    "удовлетворительный",
    "хороший",
    "отличный",
)


def describe_work_type(work_type: str) -> str:
    match work_type:
        case "exam":
            return "экзаменационная работа"
        case "practice":
            return "практическая работа"
        case "project":
            return "проектная работа"
        case _:
            return "неизвестный тип работы"


def classify_result(score: int, work_type: str, absences: int) -> str:
    if not (0 <= score <= 100) or not (0 <= absences <= 5):
        return "Ошибка: некорректный диапазон данных"

    if score >= 90:
        level_index = 3
    elif score >= 75:
        level_index = 2
    elif score >= 60:
        level_index = 1
    else:
        level_index = 0

    if absences > 3 and level_index > 0:
        level_index -= 1

    work_description = describe_work_type(work_type)
    return f"Уровень: {LEVELS[level_index]}; {work_description}"


def run_tests() -> None:
    test_cases = [
        ((0, "exam", 0), "Уровень: недостаточный; экзаменационная работа"),
        ((59, "practice", 2), "Уровень: недостаточный; практическая работа"),
        ((60, "project", 3), "Уровень: удовлетворительный; проектная работа"),
        ((74, "exam", 0), "Уровень: удовлетворительный; экзаменационная работа"),
        ((75, "practice", 1), "Уровень: хороший; практическая работа"),
        ((89, "project", 0), "Уровень: хороший; проектная работа"),
        ((90, "exam", 0), "Уровень: отличный; экзаменационная работа"),
        ((100, "project", 0), "Уровень: отличный; проектная работа"),
        ((95, "exam", 4), "Уровень: хороший; экзаменационная работа"),
        ((45, "practice", 5), "Уровень: недостаточный; практическая работа"),
        ((-1, "exam", 0), "Ошибка: некорректный диапазон данных"),
        ((85, "lab", 2), "Уровень: хороший; неизвестный тип работы"),
    ]

    for idx, (args, expected) in enumerate(test_cases, start=1):
        actual = classify_result(*args)
        assert actual == expected, (
            f"Тест {idx} не пройден: {args} -> получено {actual!r}, "
            f"ожидалось {expected!r}"
        )
        print(actual)


def main() -> None:
    run_tests()
    print("Задание 1: все 12 тестовых сценариев успешно пройдены.")
    for sample in [(95, "exam", 4), (60, "project", 3), (85, "lab", 2), (-1, "exam", 0)]:
        print(f"  {sample} -> {classify_result(*sample)}")


if __name__ == "__main__":
    run_tests()
    main()