# Customer retention findings

This descriptive portfolio case study uses IBM's public Telco Customer Churn sample. The unit is one customer record; the file is a snapshot, with no dependable event dates for a time trend.

## Executive readout

- 1,869 of 7,043 customers are labeled churned: **26.54%**. The remaining 5,174 are labeled active.
- Month-to-month customers have **42.71%** observed churn (1,655 / 3,875), versus **11.27%** for one-year and **2.83%** for two-year contracts. Month-to-month accounts represent 88.55% of all churned customers.
- Customers with 0–12 months tenure have **47.44%** churn (1,037 / 2,186), versus **9.51%** for 49–72 months (213 / 2,239). This suggests an onboarding investigation, subject to cohort and survivorship effects.
- Electronic-check customers have **45.29%** observed churn (1,071 / 2,365). Fiber-optic customers have **41.89%** (1,297 / 3,096). These segments overlap; their counts must not be added.
- Monthly charges attached to churned records total **139,130.85** in the source's charge units. This is an exposure proxy, not measured lost revenue, a forecast, or a causal effect. No currency or reporting date is assumed.

## Decisions to investigate

Prioritize qualitative research and onboarding diagnostics for short-tenure, month-to-month customers. Explore billing experience among electronic-check users and service experience among fiber-optic users. Test any retention intervention with a controlled experiment before attributing an improvement to it. Validate contact permissions, economics and eligibility in real operational data before outreach.

## Quality and limitations

All 7,043 customer IDs are unique. Eleven TotalCharges values are blank and belong to zero-tenure records; they remain null and are excluded from any total-charge average. They are not replaced with zero. MonthlyCharges and churn indicators have no missing values. Python calculations are independently reconciled against SQLite aggregations. Segment rates use the selected segment's customer count as denominator. Churn labels are observed outcomes, not model scores. No customer-level risk ranking is produced, and the sample should not be represented as client or employment work.
