import math

class ShapeCalculator:
    @staticmethod
    def circle_area(radius):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return math.pi * radius**2

    @staticmethod
    def triangle_area(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Длины сторон должны быть положительными числами")
        
        # Проверка на прямоугольность треугольника
        sides = [a, b, c]
        sides.sort()
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            is_right_triangle = True
        else:
            is_right_triangle = False
        
        # Вычисление площади треугольника по формуле Герона
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        return area, is_right_triangle

if __name__ == "__main__":
    calculator = ShapeCalculator()
    
    
    circle_radius = 5
    circle_area = calculator.circle_area(circle_radius)
    print(f"Площадь круга с радиусом {circle_radius} равна {circle_area:.2f}")
    
    
    triangle_a = 3
    triangle_b = 4
    triangle_c = 5
    triangle_area, is_right_triangle = calculator.triangle_area(triangle_a, triangle_b, triangle_c)
    print(f"Площадь треугольника с сторонами {triangle_a}, {triangle_b}, {triangle_c} равна {triangle_area:.2f}")
    if is_right_triangle:
        print("Треугольник является прямоугольным.")
    else:
        print("Треугольник не является прямоугольным.")
