# Mindbox_task
# Product Category Analysis and Shape Calculator

This Python project leverages Apache Spark (PySpark) for product-category analysis and provides a ShapeCalculator class for calculating the areas of circles and triangles.

## Product-Category Analysis

The product-category analysis section of this project uses PySpark to process product and category data. It performs the following tasks:

1. **Creating a SparkSession**: A SparkSession is created to initialize Spark.

2. **Creating DataFrames**: Two DataFrames are created—one for products and another for categories. The product DataFrame contains product names and their associated categories, while the category DataFrame contains category names.

3. **Exploding Categories**: The product DataFrame is transformed to expand the list of categories into separate rows using the `explode` function.

4. **Joining DataFrames**: The exploded product DataFrame is joined with the category DataFrame to associate product names with their corresponding category names. This creates a new DataFrame that includes all product-category pairs, including products without categories.

5. **Displaying the Result**: The resulting DataFrame is displayed to show all product-category pairs.

## Shape Calculator

The ShapeCalculator class provides methods for calculating the areas of circles and triangles. It offers the following functionality:

- `circle_area(radius)`: Calculates the area of a circle given its radius.

- `triangle_area(a, b, c)`: Calculates the area of a triangle given its side lengths and checks if the triangle is a right triangle.

## Usage

### Product-Category Analysis

1. Install the required dependencies, including Apache Spark, if not already installed.

2. Run the provided code to perform product-category analysis using PySpark.

### Shape Calculator

1. Import the `ShapeCalculator` class into your Python project.

2. Create an instance of `ShapeCalculator`.

3. Use the `circle_area(radius)` method to calculate the area of a circle by providing its radius as an argument.

4. Use the `triangle_area(a, b, c)` method to calculate the area of a triangle by providing the lengths of its sides as arguments. The method also returns whether the triangle is a right triangle.

```python
# Example usage of ShapeCalculator
from your_module import ShapeCalculator

calculator = ShapeCalculator()

circle_radius = 5
circle_area = calculator.circle_area(circle_radius)
print(f"The area of a circle with radius {circle_radius} is {circle_area:.2f}")

triangle_a = 3
triangle_b = 4
triangle_c = 5
triangle_area, is_right_triangle = calculator.triangle_area(triangle_a, triangle_b, triangle_c)
print(f"The area of a triangle with sides {triangle_a}, {triangle_b}, {triangle_c} is {triangle_area:.2f}")
if is_right_triangle:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
