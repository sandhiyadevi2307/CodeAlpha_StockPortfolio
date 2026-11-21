
# CodeAlpha Task 2 - Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 190
}

# Store portfolio details
portfolio = {}
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

# Display available stocks
print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

# Get stock details from user
while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Please enter a positive quantity!")
                continue

            investment = stock_prices[stock_name] * quantity

            portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

            total_investment += investment

            print("Stock added successfully!")
            print("Investment value: $", investment)

        except ValueError:
            print("Please enter a valid number!")

    else:
        print("Invalid stock name! Please try again.")

# Display portfolio
print("\n===== YOUR STOCK PORTFOLIO =====")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity

    print(stock, "| Quantity:", quantity, "| Value: $", value)

# Display total investment
print("\nTotal Investment: $", total_investment)

# Save portfolio in a text file
with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO REPORT\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity

        file.write(
            f"{stock} | Quantity: {quantity} | Value: ${value}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nPortfolio saved successfully in portfolio.txt")