# Supply Chain Correlation Analysis

This repository contains the correlation analysis of key supply chain metrics collected from 61 procurement transactions of a major automotive manufacturer over the past quarter.

## Dataset Description

The dataset includes the following critical supply chain variables:

- **Supplier_Lead_Time:** Days from order placement to delivery
- **Inventory_Levels:** Current stock quantities (units)
- **Order_Frequency:** Number of orders placed per month
- **Delivery_Performance:** On-time delivery rate (%)
- **Cost_Per_Unit:** Unit cost in dollars ($)

## Contents of the Repository

- `q-excel-correlation-heatmap.xlsx`: Excel workbook with raw supply chain data and correlation matrix calculations.
- `correlation.csv`: Exported correlation matrix values generated using Excel’s Data Analysis ToolPak.
- `heatmap.png`: Screenshot of the correlation matrix with conditional formatting applied as a heatmap, highlighting strong positive (green), weak (white), and negative (red) correlations.

## How to Reproduce the Analysis

1. Enable Excel's Data Analysis ToolPak:
   - Go to **File → Options → Add-ins**.
   - Select **Excel Add-ins** from Manage dropdown and click **Go**.
   - Check **Analysis ToolPak** and hit **OK**.

2. Generate the Correlation Matrix:
   - Select **Data → Data Analysis → Correlation**.
   - Input Range: Select your full dataset including headers.
   - Check **Labels in first row**.
   - Output Range: New worksheet or specified cell.
   - Click **OK**.

3. Apply Conditional Formatting for Heatmap:
   - Select the correlation values in the matrix (exclude headers).
   - Go to **Home → Conditional Formatting → Color Scales**.
   - Choose the **Red-White-Green** color scale.
   - This visually highlights correlations from -1 (red) to +1 (green).

4. Save the correlation matrix as CSV (`correlation.csv`) for data sharing.
5. Capture a clear screenshot of the heatmap area (`heatmap.png`) for visualization.

## Purpose & Insights

This analysis helps identify how different supply chain metrics interact, assisting in bottleneck identification, delivery prediction, and cost optimization. Strong correlations signify metrics moving together, guiding strategic operational decisions.

## Contact

For any questions or collaborations, please reach out to:  
**24f1002092@ds.study.iitm.ac.in**
