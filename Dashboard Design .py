print("DATA ANALYST INTERNSHIP")
print("======================")

sales = [12000, 15000, 14000, 18000, 22000, 25000]
profit = [3000, 4000, 3500, 5000, 6500, 7500]

total_sales = sum(sales)
total_profit = sum(profit)

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

growth = ((sales[-1] - sales[0]) / sales[0]) * 100

print("Sales Growth:", round(growth, 2), "%")
print("Dashboard completed")