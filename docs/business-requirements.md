# Customer retention reporting brief

**Audience:** a retention manager and business analyst reviewing a sample customer base.

**Questions:** How many customers churned? Which contract, tenure, payment and service segments have the highest observed rates? How do rates differ from absolute customer counts and associated monthly charges?

**Grain:** one customer snapshot record. No date field supports calendar trends or cohort retention curves.

**Definitions:** Customer count is the sum of a constant-one column. Churned customers is the sum of a Yes/No indicator. Active customers is the complementary No indicator. Churn rate is churned customers divided by customer count in the same current filter context. Average monthly charge is the arithmetic mean over customer records. Churned monthly charges is the sum of MonthlyCharges only for Yes records; it does not estimate future losses. Contract and service filters must change the numerator and denominator together.

**Acceptance:** KPI totals reconcile with the cleaned source and independent SQL; segment counts sum to 7,043; a contract filter reproduces the corresponding source summary; exported pages remain legible without clipping; default export has all customers selected.

**Data provenance:** IBM Telco Customer Churn sample, downloaded 2026-10-24 from https://github.com/IBM/telco-customer-churn-on-icp4d/blob/master/data/Telco-Customer-Churn.csv. The original file and upstream Apache 2.0 license are retained under data/. This case study is an independently authored portfolio exercise. It does not imply work for IBM, a telecom client, or measured retention improvements.
