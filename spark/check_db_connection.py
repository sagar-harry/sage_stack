from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("DatabaseConnectionTest") \
    .config("spark.driver.extraClassPath", "mysql-connector-j-8.1.0.jar") \
    .getOrCreate()



# Define the JDBC URL
jdbc_url = "jdbc:mysql://mysql_container:3306/genaidb"

# Define the connection properties
connection_properties = {
    "user": "root",
    "password": "root",
    "driver": "com.mysql.cj.jdbc.Driver"
}

table_name = "health_care_data"
df = spark.read.jdbc(url=jdbc_url, table=table_name, properties=connection_properties)

df.show()

spark.stop()