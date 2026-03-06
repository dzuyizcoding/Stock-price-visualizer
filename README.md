# Stock-price-visualizer
A Python-based financial data visualization tool that fetches historical stock prices for selected Hong Kong blue-chip companies and generates visual charts of their recent performance.

The program retrieves market data using the **yFinance API**, processes the dataset with **Pandas**, and produces multi-panel visualizations using **Matplotlib** to display stock trends over the last 10 trading days.

---
## 🚀 Features

- Fetches historical stock price data from Yahoo Finance
- Processes and cleans financial data using **Pandas**
- Automatically exports structured datasets to **CSV**
- Generates multi-panel **Matplotlib charts** for visualizing stock price trends
- Displays the most recent **10 trading days** of market activity
- Includes logging and error handling to ensure reliable execution

---
## 🛠 Tech Stack

- **Python**
- **Pandas**
- **Matplotlib**
- **yFinance**

---
## 📊 Example Output

The program generates two outputs:

**1. CSV Dataset**
### Example CSV Output

The program exports stock price data to a CSV file in the following format:

```csv
Date,0001,0002,0003,0005
2026-02-23,64.25,77.40,7.69,135.90
2026-02-24,62.55,77.00,7.69,135.30
2026-02-25,62.00,75.05,7.62,142.70
2026-02-26,64.80,73.40,7.53,145.00
2026-02-27,64.40,74.20,7.61,147.30
2026-03-02,62.65,74.15,7.56,139.70
2026-03-03,62.65,74.80,7.70,135.80
2026-03-04,59.85,73.35,7.54,130.80
2026-03-05,61.15,74.55,7.53,133.90
2026-03-06,60.70,74.45,7.52,133.40

**2. Chart Visualization**

A multi-panel chart displaying price movements for each stock across the last 10 trading days.

<img width="2069" height="1029" alt="stock_prices" src="https://github.com/user-attachments/assets/d09f0f99-97d4-474d-b6b3-f69b6e5b6da1" />


---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/stock-price-visualizer.git
cd stock-price-visualizer
```
## Install dependencies:
```bash
pip install pandas matplotlib yfinance
```
## ▶️ Run the Program
``` bash
python stock_price_visualizer.py
```
## 📂 Project Structure
stock-price-visualizer
│
├── stock-price-visualizer.py
├── stock_prices.cs
├── stock_prices.png
└── README.md
##💡Future Improvements
- Add interactive charts using Plotly
- Support additional stock markets and tickers
- Build a web dashboard for real-time visualization
- Implement automated daily data updates
