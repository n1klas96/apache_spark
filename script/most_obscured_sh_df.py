from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("MostObscuredSuperhero").getOrCreate()

schema = StructType([ \
                     StructField("id", IntegerType(), True), \
                     StructField("name", StringType(), True)])

names = spark.read.schema(schema).option("sep", " ").csv("Marvel+Names.txt")

lines = spark.read.text("Marvel+Graph.txt")

# Small tweak vs. what's shown in the video: we trim each line of whitespace as that could
# throw off the counts.
connections = lines.withColumn("id", func.split(func.trim(func.col("value")), " ")[0])  \
    .withColumn("connections", func.size(func.split(func.trim(func.col("value")), " ")) - 1) \
    .groupBy("id").agg(func.sum("connections").alias("connections"))
    
min_connections_count = connections.agg(func.min("connections")).first()[0]

min_connections = connections.filter(func.col("connections") == min_connections_count)
 
min_connections_names = min_connections.join(names, "id")

print("the following charakters have only" + str(min_connections_count) + "connections: ")
    
min_connections_names.select("name").show()

 
 
   
#mostPopular = connections.sort(func.col("connections").desc()).first()

mostObscuredName = names.filter(func.col("id") == connections).select("name").first().show()

#print(mostPopularName[0] + " is the most popular superhero with " + str(mostPopular[1]) + " co-appearances.")