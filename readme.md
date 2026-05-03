# AWS Medallion Analytics Architecture: CloudScale Pipeline

🚀 **Project Overview**
This project implements a fully automated, end-to-end data pipeline on AWS designed to process large-scale marketplace data. By leveraging the **Medallion (Bronze/Silver/Gold) Architecture**, the pipeline transforms raw transaction data into high-performance, cost-optimized datasets for business intelligence.

## 🏗️ Architecture Diagram
![Architecture](architecture.png)

---

## 🛠️ Technical Stack & Tools
*   **Storage:** AWS S3 (Landing, Bronze, and Gold zones).
*   **Compute/ETL:** AWS Glue (PySpark) for schema enforcement and data transformation.
*   **Query Engine:** AWS Athena for serverless SQL analytics.
*   **Format:** Optimized Apache Parquet with Snappy compression.
*   **Partitioning:** Hive-style partitioning by `Year/Month/Day`.

---

## 🛠️ Technical Pipeline Breakdown

### 1. Data Ingestion (Landing Zone)
*   **Role:** Entry point for raw, immutable data sources.
*   **Action:** Python/Boto3 scripts automate the ingestion of `raw_users.csv`, `raw_events.csv`, and `raw_subscriptions.csv`.

### 2. Processing & Cataloging (Silver Layer)
*   **Role:** Schema enforcement, data cleaning, and metadata management.
*   **Tools:** AWS Glue (PySpark) & Glue Data Catalog.
*   **Operations:** Type conversion, deduplication, and automated schema discovery via Glue Crawlers.

### 3. Optimized Data Lake (Gold Zone)
*   **Role:** Hosting analytics-ready, partitioned datasets.
*   **Impact:** Transitioned storage from CSV to **Parquet**, reducing query data scans by **over 90%** and significantly lowering AWS costs.

---

## 📈 Business KPIs Delivered
The pipeline automates critical business metrics using SQL-driven analysis in Amazon Athena:
*   **Monthly Recurring Revenue (MRR):** Automated tracking of subscription revenue growth.
*   **User Engagement:** Advanced analysis of active user trends and churn rates.
*   **Performance:** High-speed querying via partitioned datasets.

---

## 📂 Project Structure
```text
/cardmarket-data-pipeline
├── architecture.png         # Technical Architecture Diagram
├── /scripts
│   └── glue_etl_job.py      # PySpark ETL transformation logic
├── /sql
│   ├── mrr_report.sql       # Athena SQL for Revenue KPIs
│   └── user_engagement.sql  # Athena SQL for Churn analysis
├── /data_samples            # Small-scale samples (~5-10 rows)
│   ├── raw_users_sample.csv
│   └── mrr_output_sample.csv
└── README.md                # Project documentation
