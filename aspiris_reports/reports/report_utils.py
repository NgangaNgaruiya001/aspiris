# reports/report_utils.py

import pandas as pd
from collections import defaultdict

def compute_sales_report(sales, targets):
    # Identify region columns
    region_columns = targets.columns[2:]  # Exclude 'Month' and 'Sub-division'
    
    # Initialize a list to store results
    report_data = []

    for region in region_columns:
        for _, row in targets.iterrows():
            month = row['Month']
            sub_division = row['Sub-division']
            target_value = row[region]

            # Filter sales data for this region, month, and sub-division
            sales_data = sales[
                (sales['Month'] == month) &
                (sales['Region'] == region) &
                (sales['Sub-division'] == sub_division)
            ]

            actual_sales = sales_data['Sales'].sum()

            report_data.append({
                'Month': month,
                'Region': region,
                'Sub-division': sub_division,
                'Target': target_value,
                'Actual Sales': actual_sales,
                'Variance': actual_sales - target_value
            })

    # Convert the result to a DataFrame
    report_df = pd.DataFrame(report_data)
    return report_df
