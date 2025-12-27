import os
import urllib.request
import ssl

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

data_dir1 = "hadoop/bin"
os.makedirs(data_dir1, exist_ok=True)

# ======================================================================================
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys

python_path = sys.executable
os.environ['PYSPARK_PYTHON'] = python_path
os.environ['HADOOP_HOME'] ="hadoop"
os.environ['JAVA_HOME'] = r'C:\Users\Dell\.jdks\jbr-17.0.14'
######################🔴🔴🔴################################

#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.12:3.5.1 pyspark-shell'
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-avro_2.12:3.5.4 pyspark-shell'
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 pyspark-shell'

conf = SparkConf().setAppName("pyspark").setMaster("local[*]").set("spark.driver.host","localhost").set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

spark = SparkSession.builder.getOrCreate()

spark.read.format("csv").load("data/test.txt").toDF("Success").show(20, False)

##################🔴🔴🔴🔴🔴🔴 -> DON TOUCH ABOVE CODE -- TYPE BELOW ####################################
#second highest salary

data = [

    ("DEPT1", 101),
    ("DEPT1", 100),
    ("DEPT1", 101),
    ("DEPT2", 100),
    ("DEPT2", 102),
    ("DEPT3", 100),
    ("DEPT3", 104)
]

columns = ["department", "salary"]

df = spark.createDataFrame(data, columns)

df.show()

from pyspark.sql.window import Window
from pyspark.sql.functions import *


windowcreate = Window.partitionBy("department").orderBy(col("salary").desc())
denserankdf =  df.withColumn("rnk", dense_rank().over(windowcreate))
finaldf =  denserankdf.filter("rnk = 2").drop("rank")
finaldf.show()


data = [
    (101, 5001, "2025-08-01 10:00", 1200, "web"),
    (101, 5002, "2025-08-03 09:14", 800, "app"),
    (101, 5003, "2025-08-05 21:05", 2200, "web"),
    (102, 6001, "2025-08-02 08:30", 2500, "app"),
    (102, 6002, "2025-08-02 09:00", 450, "app"),
    (102, 6003, "2025-08-06 12:10", 900, "web"),
    (103, 7001, "2025-08-04 17:45", 300, "web")
]
schema = ["user_id","order_id","event_ts","amount","channel"]
df = spark.createDataFrame(data, schema)
df.show()

from pyspark.sql.window import Window
from pyspark.sql.functions import *
windowCreate = Window.partitionBy("user_id").orderBy("event_ts").orderBy(col("amount").desc())

result = (
    df
     .withColumn("row_num",row_number().over(windowCreate))
     .withColumn("densee_rank",dense_rank().over(windowCreate.orderBy(col("amount").desc())))
     .withColumn("rankk",rank().over(windowCreate.orderBy(col("amount").desc())))
     .withColumn("ntile",ntile(3).over(windowCreate.orderBy(col("amount").desc())))
     .withColumn("lagg",lag("amount",1).over(windowCreate))
     .withColumn("lead",lead("amount",1).over(windowCreate))

    .withColumn("max",max("amount").over(windowCreate))
     .filter(col("amount")==col("max"))
)
result.show()

max_amt = df.agg(max("amount").alias("max_amt")).collect()[0]["max_amt"]
max_df =   df.filter(col("amount") == max_amt)
max_df.show()
#  Register the DataFrame as a SQL table
df.createOrReplaceTempView("employees")
# Write the SQL query
second_highest_salary_sql = spark.sql("""
SELECT user_id, order_id, amount
FROM (
  SELECT *,
         ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY amount DESC) AS row_num
  FROM employees
) subquery
WHERE row_num = 2
""")
second_highest_salary_sql.show()

wincreate = Window.partitionBy("user_id").orderBy(col("amount").desc())
denserank = df.withColumn("rnk",row_number().over(wincreate))
filterrank=denserank.filter(col("rnk")==1)
filterrank.show()

orderdf = df.orderBy(col("amount").desc())
second_highest_salary = orderdf.collect()[5]["amount"]
filterdf =df.filter(col("amount")== second_highest_salary)
filterdf.show()

data =[
               (1 , 6000, 2018 ),
               (1 , 7000, 2019 ),
               (1 , 7500, 2020 ),
               (1 , 7000, 2021),
               (2 , 6000, 2018 ),
               (2 , 7000, 2019 ),
               (3 , 7500, 2020 ),
               (3 , 8000, 2021),
      ]
schema=("empid","sal","year")
dfCreate=spark.createDataFrame(data,schema)
from pyspark.sql.window import Window
from pyspark.sql.functions import *

windowCreate = Window.partitionBy("empid").orderBy("year")

lagDf = dfCreate.withColumn("lagColumn",lag("sal",1).over(windowCreate))

lagDf.show()
diffDf = (lagDf.withColumn("diffSal",expr("sal - lagColumn")).coalesce(1)
               .withColumn("diffSal",coalesce("diffsal",lit(0))))
diffDf.show()
"""df_clean = diffDf.na.fill(0)
df_clean.show()
col=diffDf.coalesce(1)
col.show()"""