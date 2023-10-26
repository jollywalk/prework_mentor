import yfinance as yf
import pandas as pd

def fetch_data(stock_symbol):
    # Fetch historical data
    data = yf.download(stock_symbol, period="1y", interval="1d")
    return data

def analyze_moving_averages(data):
    # Calculate 50-day moving average
    data['50_MA'] = data['Close'].rolling(window=50).mean()
    
    # Calculate 200-day moving average
    data['200_MA'] = data['Close'].rolling(window=200).mean()

    latest_50_MA = data['50_MA'].iloc[-1]
    latest_200_MA = data['200_MA'].iloc[-1]

    if latest_50_MA > latest_200_MA:
        return latest_50_MA, latest_200_MA, 'Golden Crossover'
    elif latest_50_MA < latest_200_MA:
        return latest_50_MA, latest_200_MA, 'Death Cross'
    else:
        return latest_50_MA, latest_200_MA, 'No clear trend'

def main():
    stock_symbol = "NUCLEUS.NS"  
    data = fetch_data(stock_symbol)
    ma_50, ma_200, trend = analyze_moving_averages(data)
    
    print(f"50 DMA for {stock_symbol}: {ma_50}")
    print(f"200 DMA for {stock_symbol}: {ma_200}")
    print(f"Trend identified: {trend}")

if __name__ == "__main__":
    main()
