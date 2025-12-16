# Basic variables
leads = 120
conversion_rate = 0.25
company_name = "ACME SaaS"
is_profitable = True
revenue = 10000

# Discovering types (widely used in debugging)
print(type(leads))
print(type(conversion_rate))
print(type(company_name))
print(type(is_profitable))

# Multiple assignment
monthly_leads, monthly_deals, monthly_revenue = 100, 25, 50000

# Reassignment
monthly_revenue += 10000
print(monthly_revenue)

# Naming conventions
# Wrong
TotalRevenue = 10000
x = 5

# Correct
total_revenue = 10000
monthly_active_users = 320

# Sales Analytics example
leads = 200
conversion_rate = 0.15

estimated_deals = leads * conversion_rate
print("Estimated deals:", estimated_deals)
