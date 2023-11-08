import yfinance as yf

# Initialize an empty portfolio as a dictionary
portfolio = {}

# Function to add a stock to the portfolio
def add_stock(symbol, quantity, purchase_price):
    try:
        stock_data = yf.Ticker(symbol)
        current_price = stock_data.history(period="1d")["Close"].iloc[0]
    except:
        print(f"Stock with symbol {symbol} not found.")
        return

    if symbol not in portfolio:
        portfolio[symbol] = {'quantity': quantity, 'purchase_price': purchase_price}
    else:
        portfolio[symbol]['quantity'] += quantity
        portfolio[symbol]['purchase_price'] = ((portfolio[symbol]['quantity'] - quantity) * portfolio[symbol]['purchase_price'] + quantity * purchase_price) / portfolio[symbol]['quantity']

# Function to remove a stock from the portfolio
def remove_stock(symbol, quantity):
    if symbol in portfolio:
        quantity = int(input("Enter the quantity of shares to remove: "))
        if quantity >= portfolio[symbol]['quantity']:

            del portfolio[symbol]
        else:
            portfolio[symbol]['quantity'] -= quantity
    else:
        print(f"Stock with symbol {symbol} not found in the portfolio.")

# Function to calculate the total portfolio value
def calculate_portfolio_value():
    total_value = 0
    for symbol, stock in portfolio.items():
        try:
            stock_data = yf.Ticker(symbol)
            current_price = stock_data.history(period="1d")["Close"].iloc[0]
            total_value += current_price * stock['quantity']
        except:
            print(f"Error fetching data for stock with symbol {symbol}.")
    return total_value

# Function to display the portfolio
def display_portfolio():
    print("Stock Portfolio:")
    print("Symbol\tQuantity\tPurchase Price")
    for symbol, stock in portfolio.items():
        print(f"{symbol}\t{stock['quantity']}\t\t{stock['purchase_price']:.2f}")
    print(f"Total Portfolio Value: ${calculate_portfolio_value():.2f}")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. Display Portfolio")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        symbol = input("Enter the stock symbol: ")
        quantity = int(input("Enter the quantity of shares: "))
        purchase_price = float(input("Enter the purchase price per share: "))
        add_stock(symbol, quantity, purchase_price)
    elif choice == '2':

        symbol = input("Enter the stock symbol to remove: ")
        remove_stock(symbol, quantity)
    elif choice == '3':
        display_portfolio()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
