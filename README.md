# Fabric Waste Analytics Project

## 📌 Overview
An end-to-end **Microsoft Fabric Data Engineering** solution for waste pickup analytics.  
Raw CSV data is ingested into a Lakehouse, cleaned with PySpark notebooks, modeled into a star schema, and visualized in Power BI dashboards.  
The pipeline follows the **Medallion Architecture** (Bronze → Silver → Gold) and is orchestrated daily with Data Factory.

---

## 🏗️ Architecture
- **Bronze Layer**: Raw CSV files (pickups, customers, trucks)
- **Silver Layer**: Cleaned Delta tables (duplicates, nulls, invalids removed)
- **Gold Layer**: Star schema (fact + dimensions)
- **Semantic Model**: DAX measures and relationships
- **Power BI Report**: KPIs, charts, slicers
- **Pipeline**: Automated daily run (Notebook 0 → Notebook 1 → Notebook 2)

---

## 📂 Source Data
- `pickups.csv`: pickup_id, customer_id, truck_id, pickup_date, waste_type, weight_kg, cost  
- `customers.csv`: customer_id, name, city, industry  
- `trucks.csv`: truck_id, driver, capacity_kg  

---

## ⚙️ Steps Implemented
1. **Workspace Setup** → Created `ws_waste_analytics`  
2. **Lakehouse** → Created `lh_waste`  
3. **Bronze Data Generation** → Notebook `nb_00_generate_data`  
4. **Bronze → Silver Cleaning** → Notebook `nb_01_bronze_to_silver`  
5. **Silver → Gold Modeling** → Notebook `nb_02_silver_to_gold`  
6. **Semantic Model** → Created `sm_waste` with relationships & measures  
7. **Power BI Dashboard** → KPIs, charts, slicers (city, industry, waste_type)  
8. **Pipeline Orchestration** → `pl_waste_daily` scheduled daily at 6:00 AM  

---

## 📊 Power BI Dashboard Highlights
- **Cards**: Total Weight, Total Cost, Cost per Ton  
- **Line Chart**: Monthly waste trend  
- **Donut Chart**: Waste type distribution  
- **Bar Chart**: Top 10 customers by cost  
- **Table/Bar**: Truck driver pickup counts  
- **Slicers**: City, Industry, Waste Type  

---

## 🚀 How to Run
- Clone repo and open in Microsoft Fabric workspace.  
- Attach Lakehouse `lh_waste` to notebooks.  
- Run pipeline `pl_waste_daily` or trigger notebooks manually.  
- Open Power BI report `Waste Analytics Dashboard`.  

---

## 💡 Interview Pitch
*"I built an end-to-end Fabric solution: raw CSVs into a Lakehouse using a medallion architecture, PySpark cleaning into Delta tables, a star schema, a DAX semantic model, a Power BI report, and a scheduled pipeline."*

---

## 📍 Author
👨‍💻 **Suresh Gadi**  
Azure Fabric Data Engineer | Hyderabad, India
