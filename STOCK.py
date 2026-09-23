# ==========================================
#       STOCK PORTFOLIO TRACKER
# ==========================================

# Stock prices
stock_prices = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOG": 140.00,
    "AMZN": 190.00,
    "MSFT": 420.00,
    "META": 500.00,
    "NFLX": 650.00
}

# User's portfolio
portfolio = {}

# Total money spent on purchases
total_invested = 0.0


# ------------------------------------------
# Function: Display available stocks
# ------------------------------------------

def show_stocks():
    print("\n========== AVAILABLE STOCKS ==========")

    for stock, price in stock_prices.items():
        print(f"{stock:<10} : ${price:.2f}")

    print("======================================")


# ------------------------------------------
# Function: Buy stock
# ------------------------------------------

def buy_stock():
    global total_invested

    show_stocks()

    stock = input("\nEnter stock symbol to buy: ").upper()

    if stock not in stock_prices:
        print("❌ Stock not found.")
        return

    try:
        quantity = int(input("Enter quantity to buy: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            return

    except ValueError:
        print("❌ Please enter a valid number.")
        return

    price = stock_prices[stock]
    cost = price * quantity

    # Add stock to portfolio
    if stock in portfolio:
        portfolio[stock]["quantity"] += quantity
        portfolio[stock]["invested"] += cost
    else:
        portfolio[stock] = {
            "quantity": quantity,
            "invested": cost
        }

    total_invested += cost

    print("\n✅ Stock purchased successfully!")
    print("Stock:", stock)
    print("Quantity:", quantity)
    print("Price per share: $", price)
    print("Total cost: $", cost)


# ------------------------------------------
# Function: Sell stock
# ------------------------------------------

def sell_stock():
    global total_invested

    if not portfolio:
        print("\n❌ Your portfolio is empty.")
        return

    show_portfolio()

    stock = input("\nEnter stock symbol to sell: ").upper()

    if stock not in portfolio:
        print("❌ You don't own this stock.")
        return

    try:
        quantity = int(input("Enter quantity to sell: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            return

    except ValueError:
        print("❌ Please enter a valid number.")
        return

    owned_quantity = portfolio[stock]["quantity"]

    if quantity > owned_quantity:
        print("❌ You cannot sell more shares than you own.")
        print("You own:", owned_quantity)
        return

    current_price = stock_prices[stock]
    sale_value = current_price * quantity

    # Calculate average purchase price
    average_price = (
        portfolio[stock]["invested"] / portfolio[stock]["quantity"]
    )

    original_cost = average_price * quantity

    profit_loss = sale_value - original_cost

    # Update portfolio
    portfolio[stock]["quantity"] -= quantity
    portfolio[stock]["invested"] -= original_cost

    total_invested -= original_cost

    if portfolio[stock]["quantity"] == 0:
        del portfolio[stock]

    print("\n✅ Stock sold successfully!")
    print("Stock:", stock)
    print("Quantity sold:", quantity)
    print("Sale value: $", round(sale_value, 2))

    if profit_loss > 0:
        print("Profit: $", round(profit_loss, 2))
    elif profit_loss < 0:
        print("Loss: $", round(abs(profit_loss), 2))
    else:
        print("No profit or loss.")


# ------------------------------------------
# Function: Show portfolio
# ------------------------------------------

def show_portfolio():

    if not portfolio:
        print("\n📂 Your portfolio is empty.")
        return

    print("\n================ YOUR PORTFOLIO ================")

    total_current_value = 0
    total_investment = 0

    print(
        f"{'Stock':<10}"
        f"{'Quantity':<10}"
        f"{'Invested':<15}"
        f"{'Current Value':<15}"
        f"{'Profit/Loss'}"
    )

    print("-" * 65)

    for stock, data in portfolio.items():

        quantity = data["quantity"]
        invested = data["invested"]

        current_price = stock_prices[stock]
        current_value = current_price * quantity

        profit_loss = current_value - invested

        total_current_value += current_value
        total_investment += invested

        print(
            f"{stock:<10}"
            f"{quantity:<10}"
            f"${invested:<14.2f}"
            f"${current_value:<14.2f}"
            f"${profit_loss:.2f}"
        )

    print("-" * 65)

    total_profit_loss = total_current_value - total_investment

    print("Total invested:    $", round(total_investment, 2))
    print("Current value:     $", round(total_current_value, 2))

    if total_profit_loss > 0:
        print("Total profit:      $", round(total_profit_loss, 2))
    elif total_profit_loss < 0:
        print("Total loss:        $", round(abs(total_profit_loss), 2))
    else:
        print("Total profit/loss: $0.00")

    print("=================================================")


# ------------------------------------------
# Function: Search stock
# ------------------------------------------

def search_stock():

    stock = input("\nEnter stock symbol: ").upper()

    if stock in stock_prices:

        print("\n========== STOCK INFORMATION ==========")
        print("Stock:", stock)
        print("Current price: $", stock_prices[stock])

        if stock in portfolio:
            quantity = portfolio[stock]["quantity"]
            print("You own:", quantity, "shares")
        else:
            print("You don't own this stock.")

        print("=======================================")

    else:
        print("❌ Stock not found.")


# ------------------------------------------
# Function: Portfolio summary
# ------------------------------------------

def portfolio_summary():

    if not portfolio:
        print("\n📂 Portfolio is empty.")
        return

    total_investment = 0
    total_value = 0

    for stock, data in portfolio.items():

        quantity = data["quantity"]
        invested = data["invested"]

        current_value = stock_prices[stock] * quantity

        total_investment += invested
        total_value += current_value

    profit_loss = total_value - total_investment

    print("\n========== PORTFOLIO SUMMARY ==========")
    print("Number of stocks:", len(portfolio))
    print("Total invested:  $", round(total_investment, 2))
    print("Current value:   $", round(total_value, 2))

    if profit_loss > 0:
        print("Profit:          $", round(profit_loss, 2))
    elif profit_loss < 0:
        print("Loss:            $", round(abs(profit_loss), 2))
    else:
        print("Profit/Loss:     $0.00")

    print("=======================================")


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

print("\n==========================================")
print("       📈 STOCK PORTFOLIO TRACKER")
print("==========================================")

while True:

    print("\n--------------- MENU ----------------")
    print("1. View Available Stocks")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. View Portfolio")
    print("5. Search Stock")
    print("6. Portfolio Summary")
    print("7. Exit")
    print("-------------------------------------")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        show_stocks()

    elif choice == "2":
        buy_stock()

    elif choice == "3":
        sell_stock()

    elif choice == "4":
        show_portfolio()

    elif choice == "5":
        search_stock()

    elif choice == "6":
        portfolio_summary()

    elif choice == "7":
        print("\n👋 Thank you for using Stock Portfolio Tracker!")
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please select 1-7.")