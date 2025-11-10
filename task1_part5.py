import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

INPUT_FILE = 'lab4_part5.xlsx'
OUTPUT_DIR = Path('report')
OUTPUT_DIR.mkdir(exist_ok=True)
FORECAST_HORIZON = 3
print("загрузка данных...")
df = pd.read_excel(INPUT_FILE)
df = df.dropna(how='all')
cols = ['date', 'year', 'year_month', 'store', 'brand', 'product', 'quantity', 'revenue', 'cost']
df = df.iloc[:, :9]  
df.columns = cols
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['date'])
df['month'] = df['date'].dt.to_period('M')
print(f"загружено {len(df)} записей")

total_sales = df.groupby('month')['revenue'].sum()
total_qty = df.groupby('month')['quantity'].sum()

prod_monthly = df.groupby(['month', 'product']).agg({
    'quantity': 'sum',
    'revenue': 'sum',
    'cost': 'sum'
}).reset_index()
prod_monthly['avg_price'] = prod_monthly['revenue'] / prod_monthly['quantity']
prod_monthly['profit'] = prod_monthly['revenue'] - prod_monthly['cost']
prod_monthly['growth_pct'] = prod_monthly.groupby('product')['revenue'].pct_change() * 100

store_monthly = df.groupby(['month', 'store']).agg({
    'quantity': 'sum',
    'revenue': 'sum'
}).reset_index()
store_summary = df.groupby('store').agg({
    'revenue': 'sum',
    'quantity': 'sum'
}).reset_index()
store_summary['avg_sales_per_point'] = store_summary['revenue'] / len(df['month'].unique())

def simple_forecast(series, periods=3):
    """Прогноз на основе среднего за последние 3 месяца"""
    if len(series) < 3:
        return [series.mean()] * periods
    return [series.tail(3).mean()] * periods

forecast_data = []
future_months = pd.period_range(
    start=total_sales.index.max() + 1,
    periods=FORECAST_HORIZON,
    freq='M'
)

for product in df['product'].unique():
    hist = prod_monthly[prod_monthly['product'] == product].set_index('month')['revenue']
    if hist.empty:
        continue
    preds = simple_forecast(hist, FORECAST_HORIZON)
    for m, p in zip(future_months, preds):
        forecast_data.append({'month': m, 'product': product, 'forecast_revenue': p})

forecast_df = pd.DataFrame(forecast_data)

print("сохранение графиков...")
plt.figure(figsize=(12, 5))
plt.plot(total_sales.index.to_timestamp(), total_sales.values, marker='o')
plt.title('динамика общего товарооборота')
plt.ylabel('выручка (руб)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig(OUTPUT_DIR / 'total_sales.png', bbox_inches='tight', dpi=150)
plt.close()

for product in df['product'].unique():
    hist = prod_monthly[prod_monthly['product'] == product]
    fut = forecast_df[forecast_df['product'] == product]
    if hist.empty:
        continue
    
    plt.figure(figsize=(10, 4))
    plt.plot(hist['month'].astype(str), hist['revenue'], label='факт', marker='o')
    plt.plot(fut['month'].astype(str), fut['forecast_revenue'], label='прогноз', marker='s', linestyle='--')
    plt.title(f'продажи: {product}')
    plt.ylabel('выручка (руб)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f'forecast_{product.replace(" ", "_")}.png')
    plt.close()

store_summary_sorted = store_summary.sort_values('revenue', ascending=False)
plt.figure(figsize=(8, 5))
plt.bar(store_summary_sorted['store'], store_summary_sorted['revenue'], color='lightblue')
plt.title('выручка по точкам реализации')
plt.ylabel('выручка (руб)')
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'store_revenue.png')
plt.close()

avg_price_pivot = prod_monthly.pivot(index='month', columns='product', values='avg_price')
plt.figure(figsize=(12, 6))
avg_price_pivot.plot(marker='o')
plt.title('средняя цена по товарам')
plt.ylabel('цена (руб)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig(OUTPUT_DIR / 'avg_price.png', bbox_inches='tight', dpi=150)
plt.close()

prod_monthly.to_csv(OUTPUT_DIR / 'analysis_by_product.csv', index=False, float_format='%.2f')
store_monthly.to_csv(OUTPUT_DIR / 'analysis_by_store.csv', index=False, float_format='%.2f')
forecast_df.to_csv(OUTPUT_DIR / 'sales_forecast.csv', index=False, float_format='%.2f')
df.to_csv(OUTPUT_DIR / 'cleaned_data.csv', index=False)

print("\nанализ завершён")
print("отчёт сохранён в папку 'report/'")
print("\nосновные файлы:")
for f in sorted(OUTPUT_DIR.iterdir()):
    print(f"  - {f.name}")