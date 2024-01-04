def perimeter_decorator(func):
    """
    Декоратор для вывода сообщения о периметре фигуры.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Периметр фигуры равен = {result}")
        return result
    return wrapper


@perimeter_decorator
def calculate_perimeter(sides):
    """
    Вычисляет периметр многоугольника.
    """
    return sum(sides)


# Пример использования
if __name__ == "__main__":
    polygon_sides = [3, 4, 5, 6]  # Пример: многоугольник с 4 сторонами

    # Вызываем декорированную функцию
    result = calculate_perimeter(polygon_sides)

    # Результат также будет возвращен, но декоратор выведет сообщение
    print(f"Периметр многоугольника: {result}")
