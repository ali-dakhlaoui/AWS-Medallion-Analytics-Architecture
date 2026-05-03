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
*   **Role:** Acts as a secure, immutable "holding area" for all raw data.
*   **Action:** Uses **Python (Boto3)** to programmatically ingest `raw_users.csv`, `raw_events.csv`, and `raw_subscriptions.csv`.
*   **Logic:** By storing data exactly as it arrives, we ensure a "System of Record" that allows for full re-processing if downstream logic changes.

### 2. Processing & Cataloging (Silver Layer)
*   **Role:** Cleans and structures the data to ensure reliability.
*   **Data Cleaning:** The **PySpark** job handles "dirty" data by fixing date formats, removing duplicate IDs, and filling null values.
*   **Schema Standardization:** Enforces strict data types (e.g., converting strings to Decimals for prices), preventing calculation errors in financial reports.
*   **AWS Glue Catalog:** Acts as a metadata layer, allowing the data to be instantly searchable and queryable without manual indexing.

### 3. Optimized Data Lake (Gold Zone)
*   **Role:** The high-speed storage layer designed specifically for analytics.
*   **Parquet Conversion:** Converts CSVs to **Apache Parquet**. As a columnar format, it allows the system to read only the necessary columns, significantly speeding up execution.
*   **Partitioning Logic:** Data is organized by `Year/Month/Day`. This allows **Amazon Athena** to skip millions of irrelevant rows, scanning only the required timeframes.
*   **Performance Impact:** This optimization reduces data scan volume by **over 90%**, directly lowering AWS operational costs.

---

## 📈 Business KPIs Delivered
The pipeline automates critical business metrics using SQL-driven analysis:
*   **Monthly Recurring Revenue (MRR):** Automated tracking of subscription revenue growth and trends.
*   **User Engagement:** Advanced analysis of active user behavior and churn rate identification.
*   **Cost Efficiency:** Maximized performance-to-cost ratio through serverless compute and optimized storage.

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
├── /data_samples            # Small-scale samples for demonstration
│   ├── raw_users_sample.csv
│   └── mrr_output_sample.csv
└── README.md                # Project documentation
