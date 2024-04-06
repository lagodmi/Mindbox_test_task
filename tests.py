import unittest
from geometry_calculator import ShapeCalculator


class TestShapeCalculator(unittest.TestCase):
    """
        Тесты библиотеки "ShapeCalculator".
    """

    def test_validation(self):
        """
            Тестирование валидации входных данных.
        """
        with self.assertRaises(ValueError):
            ShapeCalculator.calculate_circle_area("-3")
        with self.assertRaises(ValueError):
            ShapeCalculator.calculate_triangle_area("3 4 10")
        with self.assertRaises(ValueError):
            ShapeCalculator.calculate_triangle_area("a b c")

    def test_calculate_circle_area(self):
        """
            Тестирование расчета площади круга.
        """
        self.assertEqual(ShapeCalculator.calculate_circle_area("5"), 78.54)

    def test_calculate_triangle_area(self):
        """
            Тестирование расчета площади треугольника.
        """
        self.assertEqual(ShapeCalculator.calculate_triangle_area("3 4 5"), 6.0)

    def test_is_right_triangle(self):
        """
            Тестирование проверки на прямоугольный треугольник.
        """
        self.assertTrue(ShapeCalculator.is_right_triangle("3 4 5"))
        self.assertFalse(ShapeCalculator.is_right_triangle("3 4 6"))


if __name__ == '__main__':
    unittest.main()
