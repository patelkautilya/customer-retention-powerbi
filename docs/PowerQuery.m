let
    Source = Csv.Document(Web.Contents("https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"), [Delimiter=",", Columns=21, Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers, {{"tenure", Int64.Type}, {"SeniorCitizen", Int64.Type}, {"MonthlyCharges", type number}}),
    Charges = Table.TransformColumns(Types, {{"TotalCharges", each if Text.Trim(_) = "" then null else Number.FromText(_, "en-US"), type nullable number}}),
    Count = Table.AddColumn(Charges, "Customer Count", each 1, Int64.Type),
    Churned = Table.AddColumn(Count, "Churned Customers", each if [Churn] = "Yes" then 1 else 0, Int64.Type),
    Active = Table.AddColumn(Churned, "Active Customers", each if [Churn] = "No" then 1 else 0, Int64.Type),
    Exposure = Table.AddColumn(Active, "Churned Monthly Charges", each if [Churn] = "Yes" then [MonthlyCharges] else 0, type number),
    TenureBand = Table.AddColumn(Exposure, "Tenure Band", each if [tenure] <= 12 then "01 | 0-12 months" else if [tenure] <= 24 then "02 | 13-24 months" else if [tenure] <= 48 then "03 | 25-48 months" else "04 | 49-72 months", type text)
in
    TenureBand
