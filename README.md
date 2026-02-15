# NSE Paper Trading Core

A lightweight Python-based engine for fetching NSE (National Stock Exchange of India) market data and calculating quantitative metrics for paper trading and strategy analysis.

## 🚀 Features

- **Automated Data Retrieval**: Fetches real-time and historical NSE market data via `yfinance`.
- **Quantitative Metrics**: Core logic for calculating annualized volatility and other key trading metrics.
- **Multi-Level Index Handling**: Robust parsing of financial dataframes.
- **Paper Trading Engine**: Foundation for managing virtual capital and portfolios.

## 🛠 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PranavVetkar/NSE-Paper-Trading-Core.git
   cd NSE-Paper-Trading-Core
   ```

2. **Install dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```


## 📈 Quick Start

Execute the core script to generate a quantitative profile for a stock (e.g., RELIANCE):

```bash
python nse_core.py
```

## 🖥 Example Output

The script provides a clean summary of the stock's current performance:

```text
Fetching data for RELIANCE.NS...
[*********************100%***********************]  1 of 1 completed

--- NSE Quant Profile: RELIANCE ---
Current Price: ₹1418.80
Annualized Volatility: 21.15%
```

## 🏗 Core Architecture

The engine is built around the `NSEPaperEngine` class, which handles:

- **Initial Capital**: Default setup with ₹100,000 for simulation.
- **Data Acquisition**: Fetches data with customizable periods and intervals (default: 1 month, 1 hour).
- **Metric Computation**: Annualizes volatility using the square root of time (252 days * 6.5 hours).

---
*Disclaimer: This project is for educational and research purposes only. Market data and calculations are based on public APIs.*
