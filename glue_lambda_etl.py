import sys
import pandas as pd
import boto3
from io import BytesIO

# Configuration
BUCKET = cardmarket-analytics-project-unique-id # CHANGE THIS to your bucket name

s3 = boto3.client('s3')

def process_file(file_name, partition_col=None)
    # Read from Landing
    input_key = flanding{file_name}
    obj = s3.get_object(Bucket=BUCKET, Key=input_key)
    df = pd.read_csv(BytesIO(obj['Body'].read()))
    
    # Simple Cleaning Handle missing values in important columns
    if 'churned_at' in df.columns
        df['churned_at'] = df['churned_at'].fillna('Active')

    # Optimization Partitioning and saving as Parquet
    # Cardmarket values S3 partitioning and file formats (ParquetJSON)
    base_name = file_name.replace('raw_', '').replace('.csv', '')
    
    if partition_col and partition_col in df.columns
        # Save partitioned by a specific column (e.g., plan)
        output_key = fgold{base_name}
        # In a real Glue job, we use 'awswrangler' or 'df.to_parquet' with S3 support
        print(fSaving {base_name} to {output_key} with partitioning...)
    
    # For this beginner project, save the cleaned file back to Gold
    out_buffer = BytesIO()
    df.to_parquet(out_buffer, index=False)
    s3.put_object(Bucket=BUCKET, Key=fgold{base_name}{base_name}.parquet, Body=out_buffer.getvalue())

# Execute for your files
process_file(raw_users.csv)
process_file(raw_subscriptions.csv)
process_file(raw_events.csv, partition_col=event_type)

print(ETL Job Finished Successfully!)