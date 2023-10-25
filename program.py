import pandas as pd
import yfinance as yf

# Read the Excel file
df = pd.read_excel(r"C:\Users\serendipaty\OneDrive\Desktop\adani.xlsx")

# Retrieve current market prices
company_names = df['Yahoo Code']
current_prices = []


for company_name in company_names:
    ticker = yf.Ticker(company_name)
    historical_data = ticker.history()
    if not historical_data.empty:
        current_price = historical_data.tail(1)['Close'].values[0]
    else:
        current_price = None
    current_prices.append(current_price)

# Add the current market prices to the DataFrame
df['oct17'] = current_prices

# Save the modified DataFrame to a new Excel file
df.to_excel(r'C:\Users\serendipaty\OneDrive\Desktop\adani.xlsx', index=False)


