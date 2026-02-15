import yfinance as yf
import pandas as pd
import numpy as np

class NSEPaperEngine:
    def __init__(self, initial_capital=100000):
        self.capital = initial_capital
        self.portfolio = {}     
        
    def get_data(self, symbol, period="1mo", interval="1h"):
        ticker = f"{symbol.upper()}.NS"
        print(f"Fetching data for {ticker}...")
        
        data = yf.download(tickers=ticker, period=period, interval=interval, auto_adjust=True)
        
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
            
        return data

    def calculate_metrics(self, data):
        data['Returns'] = data['Close'].pct_change()
        volatility = data['Returns'].std() * np.sqrt(252 * 6.5)
        return volatility

engine = NSEPaperEngine()
reliance_data = engine.get_data("RELIANCE")

if not reliance_data.empty:
    vol = engine.calculate_metrics(reliance_data)
    print("\n--- NSE Quant Profile: RELIANCE ---")
    print(f"Current Price: ₹{reliance_data['Close'].iloc[-1]:.2f}")
    print(f"Annualized Volatility: {vol*100:.2f}%")
else:
    print("No data found. Check your internet or symbol.")