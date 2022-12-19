# About the project 

- You can access the project within this link: [Blog-Post](https://niklas.quarto.pub/httpsniklasquartopubtest/about.html)
- i used this  Udemy course to get in touch with PySpark 
[Udemy Course](https://www.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/14315200#overview)

## Introduction & Learning Path

This small project provides an introduction to Apache Spark. As part of the Big Data Processing module in my master program, I had the chance to learn something about a framework that I had no idea about. 
Within a Udemy course, I first learned how to set up a suitable environment for Spark locally. In the case of the attached blog post, I did this on a Mac environment. For Linux and Windows, the tutorial is also linked. 

I learned quite a lot about Spark, especially in terms of the Python API: PySpark. Particularly about the different operations with RDD's and the " follow-up model" Spark SQL. It was especially instructive not to distinguish between the time before Spark 3 (where RDD's were often used) and the time after (the urge to use Spark SQL/ Dataframes), but to show ways how to combine both concepts efficiently. 
After dealing with the basics around Spark and creating some queries with SparkSQL myself, I dedicated myself to the advanced examples of the course. Besides the implementation of an algrithm, which should prove the six-dgrees-of-seperation in a network, I also built a model for collaborative filtering. These examples should show that even more abstract use-cases are relatively easy to implement in PySpark, as long as you know some basic Python and the main concepts of Spark. 
Another point of my learning path was also the topic of data streaming with Spark. I am a complete beginner in this topic as well. However, the course did a good job of catching the big topic of data streaming and explaining it in an understandable way using PySpark. In my blogpost you can find an example using log data. As soon as a new file is added to the Log Data folder, various entries are automatically written to a table in the command line. 
One point I didn't find very exciting in PySpark was the Machine Learning Library MLLib. This is probably due to the fact that through the course I was primarily trying to understand the basic framework of PySpark rather than getting directly into Machine Learning of the framework. Still, the examples were interesting and sharpened my understanding of RDD's and dataframes in Spark. 
Furthermore, I learned, at least in theory, how to run Spark on a cluster. 
GraphX was mentioned in the course, but due to the fact that GraphX only runs with Scala, it didn't get much attention.

## Self Assessment

Of course, since I was completely new to Apache Spark, as I mentioned earlier, I had a lot to learn. I think the course helped me especially to understand the two concepts around RDD's and SparkSQL. This requires frequent repetition of the exercises and the creation of own scripts. Furthermore, I have learned through the course to stay on track, even if something does not work directly. I am thinking especially about the setup of Spark on my system. After this finally worked, I really started to enjoy programming with PySpark. The remaining topics like data streaming, running Spark on a cluster, etc. were exciting experiences that were a bonus for me after understanding the basic concept behind Spark.


## Apache Spark

Spark is a unified analytics engine for large-scale data processing. It provides
high-level APIs in Scala, Java, Python, and R, and an optimized engine that
supports general computation graphs for data analysis. It also supports a
rich set of higher-level tools including Spark SQL for SQL and DataFrames,
pandas API on Spark for pandas workloads, MLlib for machine learning, GraphX for graph processing,
and Structured Streaming for stream processing.

<https://spark.apache.org/>

[![GitHub Action Build](https://github.com/apache/spark/actions/workflows/build_and_test.yml/badge.svg?branch=master&event=push)](https://github.com/apache/spark/actions/workflows/build_and_test.yml?query=branch%3Amaster+event%3Apush)
[![AppVeyor Build](https://img.shields.io/appveyor/ci/ApacheSoftwareFoundation/spark/master.svg?style=plastic&logo=appveyor)](https://ci.appveyor.com/project/ApacheSoftwareFoundation/spark)
[![PySpark Coverage](https://codecov.io/gh/apache/spark/branch/master/graph/badge.svg)](https://codecov.io/gh/apache/spark)


## Online Documentation

You can find the latest Spark documentation, including a programming
guide, on the [project web page](https://spark.apache.org/documentation.html).
This README file only contains basic setup instructions.

## Building Spark

Spark is built using [Apache Maven](https://maven.apache.org/).
To build Spark and its example programs, run:

```bash
./build/mvn -DskipTests clean package
```

(You do not need to do this if you downloaded a pre-built package.)

More detailed documentation is available from the project site, at
["Building Spark"](https://spark.apache.org/docs/latest/building-spark.html).

For general development tips, including info on developing Spark using an IDE, see ["Useful Developer Tools"](https://spark.apache.org/developer-tools.html).

## Interactive Scala Shell

The easiest way to start using Spark is through the Scala shell:

```bash
./bin/spark-shell
```

Try the following command, which should return 1,000,000,000:

```scala
scala> spark.range(1000 * 1000 * 1000).count()
```

## Interactive Python Shell

Alternatively, if you prefer Python, you can use the Python shell:

```bash
./bin/pyspark
```

And run the following command, which should also return 1,000,000,000:

```python
>>> spark.range(1000 * 1000 * 1000).count()
```

## Example Programs

Spark also comes with several sample programs in the `examples` directory.
To run one of them, use `./bin/run-example <class> [params]`. For example:

```bash
./bin/run-example SparkPi
```

will run the Pi example locally.

You can set the MASTER environment variable when running examples to submit
examples to a cluster. This can be a mesos:// or spark:// URL,
"yarn" to run on YARN, and "local" to run
locally with one thread, or "local[N]" to run locally with N threads. You
can also use an abbreviated class name if the class is in the `examples`
package. For instance:

```bash
MASTER=spark://host:7077 ./bin/run-example SparkPi
```

Many of the example programs print usage help if no params are given.

## Running Tests

Testing first requires [building Spark](#building-spark). Once Spark is built, tests
can be run using:

```bash
./dev/run-tests
```

Please see the guidance on how to
[run tests for a module, or individual tests](https://spark.apache.org/developer-tools.html#individual-tests).

There is also a Kubernetes integration test, see resource-managers/kubernetes/integration-tests/README.md

## A Note About Hadoop Versions

Spark uses the Hadoop core library to talk to HDFS and other Hadoop-supported
storage systems. Because the protocols have changed in different versions of
Hadoop, you must build Spark against the same version that your cluster runs.

Please refer to the build documentation at
["Specifying the Hadoop Version and Enabling YARN"](https://spark.apache.org/docs/latest/building-spark.html#specifying-the-hadoop-version-and-enabling-yarn)
for detailed guidance on building for a particular distribution of Hadoop, including
building for particular Hive and Hive Thriftserver distributions.

## Configuration

Please refer to the [Configuration Guide](https://spark.apache.org/docs/latest/configuration.html)
in the online documentation for an overview on how to configure Spark.

## Contributing

Please review the [Contribution to Spark guide](https://spark.apache.org/contributing.html)
for information on how to get started contributing to the project.
