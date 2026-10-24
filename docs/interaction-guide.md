# Interactive Power BI walkthrough

Open the [saved explorer page](https://app.powerbi.com/groups/me/reports/e9b3b6ce-e9aa-4185-af7a-09a66ef83da8/91989315cf14f36df4b5?experience=power-bi) with the relevant Power BI account, or download the PBIX from reports/ and open it in Power BI Desktop. PDF and PNG previews are static; their buttons and charts do not respond to clicks.

## Explore a segment

1. Start with Contract = All and the contract chart at its top level. Baseline: 7,043 customers, 1,869 churned, 26.54% churn.
2. Select Fiber optic in the Charge exposure treemap. The KPI strip becomes 3,096 customers, 1,297 churned and 41.89% churn. The donut uses that selected service's denominator: 41.89% Yes and 58.11% No.
3. Click the same service tile again to clear the selection. Clicking a donut slice or contract bar also filters the other charts and KPI cards. The explorer uses explicit Filter interactions between its three charts, rather than mixing percentage denominators through cross-highlighting.
4. The Contract dropdown provides another way to narrow the customer base. Its clear-selection control restores All.

## Drill into a contract

1. Clear other selections and point to the Churn Rate chart to reveal its drill controls.
2. Turn on Drill down (single downward arrow), then select the Month-to-month bar.
3. The chart drills to Tenure Band within Month-to-month. The KPI strip becomes 3,875 customers, 1,655 churned and 42.71% churn. The four tenure rates are 51.35%, 37.72%, 32.92% and 26.02%.
4. Use Drill up to return to contracts. The next-level and expand-all controls also let viewers compare tenure alone or the entire Contract > Tenure hierarchy. Drill filters apply to the entire page.

## Navigate

The automatic page navigator at the bottom of the explorer opens the KPI dashboard, contract/tenure analysis, payment/service analysis, or the explorer itself. In report-editing mode Power BI may require Ctrl+click to follow navigation actions. Normal reading mode uses a single click.

## Design and validation

The Retention Studio theme uses teal, coral, violet and neutral backgrounds. Coral emphasizes the churn-rate KPI, and teal distinguishes active customers on the overview. Donut and treemap segments use the theme palette, labels and legends; color is supplemented with text and values.

Validated in the Power BI service reading view: Fiber optic selection, month-to-month contract drill, drill-up restoration, and navigation to the contract page. Baseline was restored before exporting. The PBIX retains the hierarchy, six explicit chart interaction settings, theme and page navigator; four PDF pages show the default snapshot. The retained source and KPI definitions remain unchanged.
