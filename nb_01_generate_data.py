#!/usr/bin/env python
# coding: utf-8

# ## nb_01_generate_data
# 
# null

# In[7]:


import pandas as pd

df = pd.read_csv("/lakehouse/default/Files/bronze/customers.csv")
print(df.head())


# In[1]:


import pandas as pd, numpy as np, os
np.random.seed(42)
path = "/lakehouse/default/Files/bronze"
os.makedirs(path, exist_ok=True)
customers = pd.DataFrame({
"customer_id": range(1, 101),
"name": [f"Customer {i}" for i in range(1, 101)],
"city": np.random.choice(["Houston","Dallas","Austin","Boston","Chicago"], 100),
"industry": np.random.choice(["Manufacturing","Healthcare","Retail","Chemical"], 100)})
trucks = pd.DataFrame({
"truck_id": range(1, 21),
"driver": [f"Driver {i}" for i in range(1, 21)],
"capacity_kg": np.random.choice([5000, 8000, 12000], 20)})
n = 5000
w = np.random.randint(100, 5000, n)
pickups = pd.DataFrame({
"pickup_id": range(1, n+1),
"customer_id": np.random.randint(1, 101, n).astype(float),
"truck_id": np.random.randint(1, 21, n),
"pickup_date": (pd.to_datetime("2026-01-01") +
pd.to_timedelta(np.random.randint(0, 270, n), unit="D")).strftime("%Y-%m-%d"),
"waste_type": np.random.choice(["Hazardous","Recyclable","Organic","Industrial"], n),
"weight_kg": w,
"cost": (w * np.random.uniform(0.2, 0.6, n)).round(2)})
# add dirty data on purpose
pickups.loc[:49, "customer_id"] = np.nan # nulls
pickups.loc[50:79, "weight_kg"] = -10 # bad weights
pickups = pd.concat([pickups, pickups.iloc[100:150]]) # duplicates
pickups.to_csv(f"{path}/pickups.csv", index=False)
customers.to_csv(f"{path}/customers.csv", index=False)
trucks.to_csv(f"{path}/trucks.csv", index=False)
print("done")

