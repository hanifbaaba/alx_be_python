income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))

monthly_savings = income - expenses
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest
print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)