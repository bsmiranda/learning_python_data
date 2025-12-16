# 02_ex_lists_deep.py
# Deep practice with lists for Sales Analytics

"""
You have a list of deal values closed during the month.
Based on this data, you need to extract insights about sales performance.
"""

# List of closed deals in the month
deal_values = [1200, 4500, 800, 15000, 3000, 2200, 5000]

# 1. Basic exploration
print("Number of deals:", len(deal_values))
print("Total revenue:", sum(deal_values))
print("Highest deal:", max(deal_values))
print("Lowest deal:", min(deal_values))

# 2. Average deal size
average_deal = sum(deal_values) / len(deal_values)
print("Average deal size:", average_deal)

# 3. Sorting for analysis
sorted_deals = sorted(deal_values)
print("Sorted deals:", sorted_deals)

# 4. Top 3 deals (important for revenue concentration analysis)
top_3_deals = sorted_deals[-3:]
print("Top 3 deals:", top_3_deals)

# 5. Bottom 3 deals
bottom_3_deals = sorted_deals[:3]
print("Bottom 3 deals:", bottom_3_deals)

# 6. Mutability: correcting a deal value (data cleaning example)
# A deal was incorrectly registered as 800, but should be 1800
deal_values[2] = 1800
print("Corrected deals:", deal_values)

# 7. New deal added to the pipeline
deal_values.append(7000)
print("Updated deal list:", deal_values)

# 8. Revenue after update
updated_total_revenue = sum(deal_values)
print("Updated total revenue:", updated_total_revenue)

# Percentage of revenue from top 3 deals
top_3_revenue = sum(top_3_deals)
revenue_share = (top_3_revenue / updated_total_revenue) * 100

print("Top 3 deals represent:", revenue_share, "% of total revenue")
