import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define the URL template for Yahoo Finance
yahoo_finance_url = "https://finance.yahoo.com/quote/{}/"

# Read the Excel file
file_path = r"C:\Users\serendipaty\OneDrive\Desktop\LTP.xlsx"  # Update with your actual file path
df = pd.read_excel(file_path)

# Function to scrape Market Cap and LTP for a Yahoo Code
def scrape_yahoo_finance_data(yahoo_code):
    url = yahoo_finance_url.format(yahoo_code)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract Market Cap (Mkt Cap)
        mkt_cap_elem = soup.find("td", {"data-test": "OPEN-VALUE-value"})
        mkt_cap = mkt_cap_elem.text if mkt_cap_elem else "N/A"
        # Extract Last Traded Price (LTP)
        ltp_elem = soup.find("td", {"data-test": "OPEN-PRICE-value"})
        ltp = ltp_elem.text if ltp_elem else "N/A"
        return mkt_cap, ltp
    else:
        return "N/A", "N/A"

# Update the DataFrame with Market Cap and LTP
for index, row in df.iterrows():
    yahoo_code = row['Yahoo Code']
    mkt_cap, ltp = scrape_yahoo_finance_data(yahoo_code)
    df.at[index, 'Mkt Cap'] = mkt_cap
    df.at[index, 'LTP'] = ltp

# Save the updated DataFrame back to the Excel file
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)

print("Updated successfully.")
