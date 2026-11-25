"""Лабораторная работа № 3. Задание 4: LEGB, изменяемые аргументы по умолчанию и замыкания."""

from collections.abc import Callable

# Global (G) — используется только для чтения
course = "Основы программирования"


def outer() -> Callable[[], str]:
    """Демонстрирует области видимости LEGB и модификацию Enclosing через nonlocal."""
    completed_labs = 0  # Enclosing (E)

    def register_lab() -> str:
        nonlocal completed_labs
        completed_labs += 1
        label = f"{course}: {completed_labs}"  # Local (L), чтение G, Built-in len() ниже
        return f"{label} (длина строки: {len(label)})"

    return register_lab


def add_result_buggy(value: int, results: list[int] = []) -> list[int]:  # noqa: B006
    """Пример ошибки с изменяемым значением аргумента по умолчанию."""
    results.append(value)
    return results


def add_result(value: int, results: list[int] | None = None) -> list[int]:
    """Исправленная версия: создает новый список и не мутирует переданный."""
    if results is None:
        results = []
    else:
        results = list(results)
    results.append(value)
    return results


def make_threshold_checker(threshold: int | float) -> Callable[[int | float], bool]:
    """Фабрика-замыкание для проверки достижения порогового балла."""

    def checker(score: int | float) -> bool:
        return score >= threshold

    return checker


def run_tests() -> None:
    """Проверяет LEGB, ошибку изменяемого аргумента, исправление и замыкания."""
    register = outer()
    first = register()
    second = register()
    assert first.startswith("Основы программирования: 1")
    assert second.startswith("Основы программирования: 2")

    # Демонстрация накопления состояния при изменяемом значении по умолчанию
    bug_call_1 = add_result_buggy(70)
    bug_call_2 = add_result_buggy(85)
    assert bug_call_1 is bug_call_2
    assert bug_call_2 == [70, 85]

    # Исправленная функция возвращает независимые списки
    safe_call_1 = add_result(70)
    safe_call_2 = add_result(85)
    assert safe_call_1 == [70]
    assert safe_call_2 == [85]

    original = [60, 75]
    extended = add_result(90, original)
    assert original == [60, 75]
    assert extended == [60, 75, 90]

    # Независимые замыкания
    is_passing = make_threshold_checker(60)
    is_excellent = make_threshold_checker(90)
    assert is_passing(60) is True
    assert is_passing(59) is False
    assert is_excellent(89) is False
    assert is_excellent(90) is True


def main() -> None:
    run_tests()
    print("Задание 4: все проверки LEGB, аргументов по умолчанию и замыканий пройдены.")
    register = outer()
    print(" ", register())
    print(" ", register())
    is_passing = make_threshold_checker(60)
    is_excellent = make_threshold_checker(90)
    print(f"  Порог 60 для 75: {is_passing(75)}, порог 90 для 75: {is_excellent(75)}")


if __name__ == "__main__":
    main()