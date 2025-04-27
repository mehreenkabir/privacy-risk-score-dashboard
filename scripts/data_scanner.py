import pandas as pd
import os

HIGH_RISK_FIELDS = ['full_name', 'email', 'ip_address', 'date_of_birth']
RETENTION_PERIOD_YEARS = 5

def scan_dataset(file_path):
    risks = 0
    df = pd.read_csv(file_path)

    # Count high-risk PII fields
    for field in HIGH_RISK_FIELDS:
        if field in df.columns:
            risks += 10

    # Check for expired records
    if 'created_at' in df.columns:
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
        expired = df[df['created_at'] < pd.Timestamp.now() - pd.DateOffset(years=RETENTION_PERIOD_YEARS)]
        if not expired.empty:
            risks += 15

    return risks

