from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

spark = SparkSession.builder.appName("CustomerSales").getOrCreate()

schema = StructType([ \
                     StructField("customerID", IntegerType(), True), \
                     StructField("itemID", IntegerType(), True), \
                     StructField("amount", FloatType(), True)])

df = spark.read.schema(schema).csv("customer-orders.csv") # load data and apply schema -> structured
df.printSchema()

columns = df.select("customerID", "amount")

total_spent = columns.groupBy("customerID").agg(func.round(func.sum("amount"), 2).alias("total_spent"))

total_sorted = total_spent.sort("total_spent")

total_sorted.show(total_sorted.count())

spark.stop()




