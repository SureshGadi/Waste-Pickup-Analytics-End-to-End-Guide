#!/usr/bin/env python
# coding: utf-8

# ## nb_02_bronze_to_silver
# 
# null

# In[1]:


from pyspark.sql.functions import *
# Pickups
p = spark.read.option("header", True).csv("Files/bronze/pickups.csv")
p = (p.dropDuplicates(["pickup_id"])
.withColumn("pickup_id", col("pickup_id").cast("int"))
.withColumn("customer_id", col("customer_id").cast("double").cast("int"))
.withColumn("truck_id", col("truck_id").cast("int"))
.withColumn("pickup_date", to_date("pickup_date"))
.withColumn("weight_kg", col("weight_kg").cast("double"))
.withColumn("cost", col("cost").cast("double"))
.filter(col("weight_kg") > 0)
.na.drop(subset=["customer_id", "pickup_date"]))
p.write.mode("overwrite").format("delta").saveAsTable("silver_pickups")
# Customers
c = (spark.read.option("header", True).csv("Files/bronze/customers.csv")
.dropDuplicates(["customer_id"])
.withColumn("customer_id", col("customer_id").cast("int"))
.withColumn("name", trim("name")))
c.write.mode("overwrite").format("delta").saveAsTable("silver_customers")
# Trucks
t = (spark.read.option("header", True).csv("Files/bronze/trucks.csv")
.dropDuplicates(["truck_id"])
.withColumn("truck_id", col("truck_id").cast("int"))
.withColumn("capacity_kg", col("capacity_kg").cast("int")))
t.write.mode("overwrite").format("delta").saveAsTable("silver_trucks")
print(p.count(), c.count(), t.count())

