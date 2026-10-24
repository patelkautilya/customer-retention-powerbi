"""Reproduce descriptive churn analysis; no predictive or causal claims."""
from pathlib import Path
import hashlib
import json
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'data/Telco-Customer-Churn.csv'
df = pd.read_csv(source)
assert len(df) == 7043 and df.customerID.is_unique
assert set(df.Churn) == {'Yes', 'No'}
df['TotalCharges'] = pd.to_numeric(df.TotalCharges, errors='coerce')
assert df.TotalCharges.isna().sum() == 11
assert df.loc[df.TotalCharges.isna(), 'tenure'].eq(0).all()
df['Customer Count'] = 1
df['Churned Customers'] = df.Churn.eq('Yes').astype(int)
df['Active Customers'] = df.Churn.eq('No').astype(int)
df['Churned Monthly Charges'] = df.MonthlyCharges.where(df.Churn.eq('Yes'), 0)
df['Tenure Band'] = pd.cut(df.tenure, [-1,12,24,48,72], labels=['01 | 0-12 months','02 | 13-24 months','03 | 25-48 months','04 | 49-72 months']).astype(str)
df.to_csv(ROOT / 'data/customers_clean.csv', index=False)
metrics = {'customers': len(df), 'churned_customers': int(df['Churned Customers'].sum()), 'active_customers': int(df['Active Customers'].sum()), 'churn_rate': float(df['Churned Customers'].mean()), 'average_monthly_charges': float(df.MonthlyCharges.mean()), 'churned_monthly_charges': float(df['Churned Monthly Charges'].sum()), 'missing_total_charges': 11, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest()}
con = sqlite3.connect(':memory:')
df.to_sql('customers', con, index=False)
sql = con.execute('SELECT COUNT(*), SUM("Churned Customers"), AVG("Churned Customers"), SUM("Churned Monthly Charges") FROM customers').fetchone()
assert sql[0] == metrics['customers'] and sql[1] == metrics['churned_customers']
assert abs(sql[2]-metrics['churn_rate']) < 1e-10
assert abs(sql[3]-metrics['churned_monthly_charges']) < 0.001
for dimension in ['Contract','Tenure Band','PaymentMethod','InternetService','TechSupport']:
    summary = df.groupby(dimension, dropna=False).agg(customers=('customerID','size'),churned_customers=('Churned Customers','sum'),churned_monthly_charges=('Churned Monthly Charges','sum'))
    summary['churn_rate'] = summary.churned_customers / summary.customers
    assert summary.customers.sum() == len(df)
    summary.to_csv(ROOT / 'reports' / (dimension.replace(' ','_') + '.csv'))
(ROOT / 'reports/metrics.json').write_text(json.dumps(metrics, indent=2)+'\n')
print(json.dumps(metrics, indent=2))
print(pd.read_csv(ROOT / 'reports/Contract.csv').to_string(index=False))
