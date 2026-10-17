#!/usr/bin/env python
# coding: utf-8

# ## nb_03_silver_to_gold
# 
# null

# In[1]:


from pyspark.sql.functions import *
p = spark.table("silver_pickups")
# Fact
fact = (p.withColumn("date_key", date_format("pickup_date", "yyyyMMdd").cast("int"))
.withColumn("cost_per_ton", round(col("cost") / (col("weight_kg")/1000), 2))
.select("pickup_id","customer_id","truck_id","date_key",
"waste_type","weight_kg","cost","cost_per_ton"))
fact.write.mode("overwrite").format("delta").saveAsTable("fact_pickups")
# Dimensions
spark.table("silver_customers").write.mode("overwrite").format("delta").saveAsTable("dim_customer")
spark.table("silver_trucks").write.mode("overwrite").format("delta").saveAsTable("dim_truck")
# Date dimension
dates = spark.sql("SELECT explode(sequence(to_date('2026-01-01'), to_date('2026-12-31'), interval 1 day)) AS date")
dim_date = (dates.withColumn("date_key", date_format("date","yyyyMMdd").cast("int"))
.withColumn("year", year("date"))
.withColumn("month_num", month("date"))
.withColumn("month_name", date_format("date","MMM"))
.withColumn("quarter", quarter("date")))
dim_date.write.mode("overwrite").format("delta").saveAsTable("dim_date")

