from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Создание Spark сессии
spark = SparkSession.builder.appName("product_category_pairs").getOrCreate()

# Загрузка данных в датафреймы products_df и categories_df

# Пример данных
# products_df: id, product_name
# categories_df: id, category_name

# Объединение продуктов и категорий по общему id
joined_df = products_df.join(categories_df, products_df.id == categories_df.id, 'outer')

# Выбор нужных колонок для результата
result_df = joined_df.select(products_df.product_name, categories_df.category_name)

# Имена всех продуктов, у которых нет категорий
products_without_categories_df = result_df.filter(col("category_name").isNull()).select("product_name").distinct()

# Вывод всех пар "Имя продукта – Имя категории" и имена продуктов без категорий
result_df.show()
products_without_categories_df.show()
