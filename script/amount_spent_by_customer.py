#### use customer-orders.csv to add up te amount spent by customer

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("CustomerSaleAmount")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    customer_id = int(fields[0])
    amount = float(fields[2])
    return (customer_id, amount)

lines = sc.textFile("customer-orders.csv")

rddMAP = lines.map(parseLine)

total_amount = rddMAP.reduceByKey(lambda x, y: (x + y)) # key value rdd for each customer 

### adding a sorted list

total_amount_sorted = total_amount.map(lambda x: (x[1], x[0])).sortByKey()


results = total_amount_sorted.collect()

for result in results:
    print(result)

### mvp customer is 68!!!