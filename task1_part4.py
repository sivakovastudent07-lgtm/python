import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

INPUT_FILE = r'C:\Python_Laby\lab4\lab4_4\my_ml_project\S7' 
OUTPUT_DIR = Path('outputs')
PLOTS_DIR = OUTPUT_DIR / 'plots'
TABLES_DIR = OUTPUT_DIR / 'tables'

fh_months = 6

col_purchase_date = 'purchase_date'
col_flight_date = 'flight_date'
col_revenue = 'revenue'

PLOTS_DIR.mkdir(parents=True, exist_ok=True)
TABLES_DIR.mkdir(parents=True, exist_ok=True)

def savefig(fig, filename):
    fig.savefig(PLOTS_DIR / filename, bbox_inches='tight', dpi=150)


def main():
    print("загрузка данных...")
    df = pd.read_excel(INPUT_FILE)
    if col_purchase_date in df.columns:
        df[col_purchase_date] = pd.to_datetime(df[col_purchase_date], errors='coerce')
    if col_flight_date in df.columns:
        df[col_flight_date] = pd.to_datetime(df[col_flight_date], errors='coerce')

    if col_purchase_date in df.columns and df[col_purchase_date].notna().any():
        print("прогнозирование выручки с использованием простого метода")

        monthly = df.groupby(df[col_purchase_date].dt.to_period('M'))[col_revenue].sum()
        monthly.index = monthly.index.to_timestamp()

        if monthly.empty:
            print("нет данных о выручке для прогнозирования")
        else:
           
            last_val = monthly.iloc[-1]
            future_idx = pd.date_range(
                start=monthly.index.max() + pd.offsets.MonthBegin(1),
                periods=fh_months,
                freq='M'
            )
            fut_series = pd.Series([last_val] * fh_months, index=future_idx)

            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(monthly.index, monthly.values, label='факт')
            ax.plot(fut_series.index, fut_series.values, label='прогноз (последнее значение)', linestyle='--')
            ax.legend()
            ax.set_title('прогноз выручки по месяцам (последнее значение)')
            savefig(fig, 'revenue_last_value_forecast.png')
            fut_series.to_csv(TABLES_DIR / 'revenue_last_value_forecast.csv')

    else:
        print('пропускаем прогнозирование выручки')

    if col_flight_date in df.columns and df[col_flight_date].notna().any():
        print("прогнозирование количества перелётов")

        flight_ts = df.groupby(df[col_flight_date].dt.date).size()
        flight_ts.index = pd.to_datetime(flight_ts.index)
        monthly_flights = flight_ts.resample('M').sum()
        monthly_flights.to_csv(TABLES_DIR / 'monthly_flight_counts.csv')

        if not monthly_flights.empty:
            n = min(3, len(monthly_flights))
            forecast_val = monthly_flights.tail(n).mean()
            future_idx = pd.date_range(
                monthly_flights.index.max() + pd.offsets.MonthBegin(1),
                periods=fh_months,
                freq='M'
            )
            forecast_simple = pd.Series([forecast_val] * fh_months, index=future_idx)

            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(monthly_flights.index, monthly_flights.values, label='факт')
            ax.plot(forecast_simple.index, forecast_simple.values, label='скользящее среднее (3 мес)', linestyle='--')
            ax.legend()
            ax.set_title('прогноз количества перелётов по месяцам (скользящее среднее)')
            savefig(fig, 'flight_counts_rolling_mean_forecast.png')
            forecast_simple.to_csv(TABLES_DIR / 'flight_counts_rolling_mean_forecast.csv')
    else:
        print('пропускаем прогнозирование перелётов')

    df.head(200).to_csv(TABLES_DIR / 'data_sample_head200.csv', index=False)

    print('\nрезультаты сохранены в папку outputs/')
    print('основные файлы:')
    for p in sorted(PLOTS_DIR.iterdir()) + sorted(TABLES_DIR.iterdir()):
        print(' ', p.name)


if __name__ == '__main__':
    main()