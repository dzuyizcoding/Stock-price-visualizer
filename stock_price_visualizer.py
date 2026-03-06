import sys
import os
import matplotlib
matplotlib.use("Agg")

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


def log(msg):
    print(msg, flush=True)


def real_time_price(stock_code):
    ticker = f"{stock_code}.HK"
    df = yf.download(ticker, period="1mo", auto_adjust=True, progress=False)
    if df.empty:
        raise ValueError(f"No data returned for {ticker}")
    df = df[["Close"]].copy()
    df.columns = [stock_code]
    df = df.sort_index(ascending=False).iloc[:10].sort_index()
    return df


if __name__ == "__main__":
    HSI = ["0001", "0002", "0003", "0005"]
    stock_names = {
        "0001": "CKH Holdings",
        "0002": "CLP Holdings",
        "0003": "HK & China Gas",
        "0005": "HSBC Holdings",
    }

    #Fetch
    log("=== Fetching stock data ===")
    price_dfs = []
    for stock_code in HSI:
        try:
            df = real_time_price(stock_code)
            price_dfs.append(df)
            log(f"  ✓ {stock_code}  {stock_names[stock_code]}")
        except Exception as e:
            log(f"  ✗ {stock_code}  ERROR: {e}")

    if not price_dfs:
        log("ERROR: No stock data fetched. Exiting.")
        sys.exit(1)

    # Merge and CSV
    merged_df = pd.concat(price_dfs, axis=1)
    merged_df.index = merged_df.index.date
    merged_df.to_csv("stock_prices.csv")
    log("\n=== Prices (HKD) ===")
    log(merged_df.to_string())
    log("\nCSV saved → stock_prices.csv")

    # Plot and save PNG
    log("Rendering chart...")
    style.use("fivethirtyeight")
    fig, axes = plt.subplots(2, 2, figsize=(14, 7))
    axes = axes.flatten()

    for i, stock_code in enumerate(merged_df.columns):
        ax = axes[i]
        ax.plot(merged_df.index, merged_df[stock_code].values,
                linewidth=2, marker="o", markersize=4)
        ax.set_title(stock_names.get(stock_code, stock_code),
                     fontsize=11, fontweight="bold", pad=6)
        ax.set_ylabel("Price (HKD)", fontsize=8)
        ax.set_xticks(merged_df.index)
        ax.set_xticklabels(
            [str(d)[5:] for d in merged_df.index],
            rotation=40, ha="right", fontsize=8
        )
        ax.tick_params(axis="y", labelsize=8)

    fig.suptitle("HK Blue-Chip Stocks — Last 10 Trading Days",
                 fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stock_prices.png")
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    log(f"Chart saved → {out_path}")

    # Open the PNG automatically with the default Windows image viewer
    os.startfile(out_path)