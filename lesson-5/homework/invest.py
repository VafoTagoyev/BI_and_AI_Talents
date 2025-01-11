def invest(amount, rate, years):
    new_amount = amount
    for year in range(years):
        new_amount += new_amount * rate / 100.0
        print(f"year {year + 1}: ${round(new_amount, 2)}")

initial_amount = float(input("Enter initial amount: "))
percentage_rate = float(input("Enter annual percentage rate: "))
number_of_years = int(input("Enter number of years: "))
invest(initial_amount, percentage_rate, number_of_years)