from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode

# Создание SparkSession
spark = SparkSession.builder.appName("ProductCategory").getOrCreate()

# Создание датафреймов с продуктами и категориями
products_data = [("Product1", ["Category1", "Category2"]),
                 ("Product2", ["Category2", "Category3"]),
                 ("Product3", ["Category1", "Category3"]),
                 ("Product4", [])]

categories_data = [("Category1", "CategoryName1"),
                   ("Category2", "CategoryName2"),
                   ("Category3", "CategoryName3")]

products_df = spark.createDataFrame(products_data, ["Product", "Categories"])
categories_df = spark.createDataFrame(categories_data, ["Category", "CategoryName"])

# Разбивка списка категорий и объединение с продуктами
exploded_products_df = products_df.select("Product", explode("Categories").alias("Category"))
result_df = exploded_products_df.join(categories_df, exploded_products_df.Category == categories_df.Category, "left")


result_df.show()

spark.stop()
