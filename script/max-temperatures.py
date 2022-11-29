### filtering rdd's 

### max temp own try


from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MaxTemperatures")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    stationID = fields[0] # define variables from data
    entryType = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0 # convert in farenheit
    return (stationID, entryType, temperature)

lines = sc.textFile("1800.csv")
parsedLines = lines.map(parseLine)
maxTemps = parsedLines.filter(lambda x: "TMAX" in x[1])
stationTemps = maxTemps.map(lambda x: (x[0], x[2])) # key value rdd with station_id and temperature
maxTemps = stationTemps.reduceByKey(lambda x, y: max(x,y)) # maximum value
results = maxTemps.collect();

for result in results:
    print(result[0] + "\t{:.2f}F".format(result[1]))
