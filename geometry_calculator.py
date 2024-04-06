import math


class ShapeCalculator:
    class ValidateArea:
        @staticmethod
        def _validate_circle(radius_str):
            """
                Валидация радиуса круга.
            """
            try:
                radius = float(radius_str)

                if radius < 0:
                    raise ValueError("Радиус должен быть положительным числом")

            except ValueError:
                raise ValueError("Радиус должен быть положительным числом")

        @staticmethod
        def _validate_triangle_sides(sides_str):
            """
                Валидация сторон треугольника.
            """
            sides = sides_str.split()

            if len(sides) != 3:
                raise ValueError("Треугольник должен иметь три стороны")

            try:
                sides = [float(side) for side in sides]
                max_side = max(sides)

                if max_side >= sum(sides) - max_side:
                    raise ValueError(
                        "Длины сторон не соответствуют треугольнику"
                    )

                if any(side <= 0 for side in sides):
                    raise ValueError(
                        "Длины сторон должны быть положительными числами"
                    )

            except ValueError:
                raise ValueError(
                    "Стороны треугольника должны быть числами и положительными"
                )

    @staticmethod
    def calculate_circle_area(radius_str):
        """
            Расчет площади круга.
        """
        ShapeCalculator.ValidateArea._validate_circle(radius_str)
        radius = float(radius_str)
        circle_area = math.pi * radius**2
        return round(circle_area, 2)

    @staticmethod
    def calculate_triangle_area(sides_str):
        """
            Расчет площади треугольника.
        """
        ShapeCalculator.ValidateArea._validate_triangle_sides(sides_str)
        a, b, c = [float(num) for num in sides_str.split()]
        per = (a + b + c) / 2
        return math.sqrt(per * (per - a) * (per - b) * (per - c))

    @staticmethod
    def is_right_triangle(sides_str):
        """
            Проверка, является ли треугольник прямоугольным.
        """
        sides = [int(num) for num in sides_str.split()]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
