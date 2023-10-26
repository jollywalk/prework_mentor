import pandas as pd
import yfinance as yf

# Load the excel file from desktop
file_path = r"C:\Users\serendipaty\OneDrive\Desktop\chem.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')

# Ensure the 'Yahoo code' column exists
if 'Yahoo code' not in df.columns:
    raise ValueError("The column 'Yahoo code' does not exist in the provided file.")

# Fetch current market prices and volumes for the stocks
def fetch_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")
        return hist["Close"].iloc[0], hist["Volume"].iloc[0]
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None, None

prices, volumes = [], []
for ticker in df['Yahoo code']:
    price, volume = fetch_data(ticker)
    prices.append(price)
    volumes.append(volume)

# Add the fetched data to the dataframe
df['oct_26'] = prices
df['oct_26_vol'] = volumes

# Save the updated dataframe back to the excel file
df.to_excel(file_path, index=False, engine='openpyxl')

print("Data updated successfully!")
