from geometry_calculator import ShapeCalculator

if __name__ == "__main__":
    flag = True

    while flag:
        shape = input("Введите:\nесли круг 0\nесли треугольник 1\nвыйти 2\n")

        if shape == "0":
            radius = input("Введите радиус круга\n")
            circle_area = ShapeCalculator.calculate_circle_area(radius)
            print(f"Площадь круга: {circle_area}")

        elif shape == "1":
            sides = input("Введите стороны треугольника через пробел\n")
            triangle_area = ShapeCalculator.calculate_triangle_area(sides)
            right_triangle = ShapeCalculator.is_right_triangle(sides)
            print(f"Площадь треугольника: {triangle_area}")

            if right_triangle:
                print("Треугольник прямоугольный")
            else:
                print("Треугольник не прямоугольный")

        elif shape == "2":
            flag = False
