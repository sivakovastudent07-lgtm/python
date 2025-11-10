import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker
import random

np.random.seed(42)
random.seed(42)
fake = Faker('ru_RU')  

YEARS = [2021, 2022, 2023, 2024, 2025]
SPECIALTIES = [
    "Прикладная информатика",
    "Программная инженерия",
    "Экономика и бух. учёт",
    "Международные отношения",
    "Биотехнологии"
]
FORMS = ["очная", "заочная"]

data = []
for year in YEARS:
    num_students = random.randint(46, 105)  
    for _ in range(num_students):
        ct1 = np.random.uniform(10, 100)
        ct2 = np.random.uniform(10, 100)
        ct3 = np.random.uniform(10, 100)
        sum_ct = ct1 + ct2 + ct3  
        school_avg = np.random.uniform(4.0, 10.0)
        total_score = sum_ct + (school_avg * 10)
        data.append({
            "ФИО": fake.name(),
            "Год поступления": year,
            "Форма обучения": random.choice(FORMS),
            "ЦТ_1": ct1,
            "ЦТ_2": ct2,
            "ЦТ_3": ct3,
            "Сумма_ЦТ": sum_ct,
            "Средний балл аттестата": school_avg,
            "Общий балл": total_score,
            "Специальность": random.choice(SPECIALTIES),
            "Адрес регистрации": fake.address(),
            "Телефон": fake.phone_number()
        })

df = pd.DataFrame(data)

plt.style.use('seaborn-v0_8')

ct1_trend = df.groupby("Год поступления")["ЦТ_1"].mean()
ct2_trend = df.groupby("Год поступления")["ЦТ_2"].mean()
ct3_trend = df.groupby("Год поступления")["ЦТ_3"].mean()

plt.figure(figsize=(10, 5))
plt.plot(ct1_trend.index, ct1_trend.values, marker='o', label='ЦТ/ЦЭ 1')
plt.plot(ct2_trend.index, ct2_trend.values, marker='s', label='ЦТ/ЦЭ 2')
plt.plot(ct3_trend.index, ct3_trend.values, marker='^', label='ЦТ/ЦЭ 3')
plt.title("Динамика среднего балла по каждому ЦТ/ЦЭ (2021–2025)")
plt.xlabel("Год")
plt.ylabel("Средний балл")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

school_trend = df.groupby("Год поступления")["Средний балл аттестата"].mean()
plt.figure(figsize=(10, 5))
plt.plot(school_trend.index, school_trend.values, marker='d', color='green', linewidth=2)
plt.title("Динамика среднего балла аттестата (2021–2025)")
plt.xlabel("Год")
plt.ylabel("Средний балл")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

passing_trend = df.groupby("Год поступления")["Общий балл"].min()
plt.figure(figsize=(10, 5))
plt.bar(passing_trend.index, passing_trend.values, color='coral', alpha=0.8, edgecolor='black')
plt.title("Динамика проходного балла (2021–2025)")
plt.xlabel("Год")
plt.ylabel("Проходной балл")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

spec_counts = df["Специальность"].value_counts()
plt.figure(figsize=(10, 6))
spec_counts.plot(kind='barh', color='skyblue', edgecolor='black')
plt.title("Количество поступивших студентов по специальностям (2021–2025)")
plt.xlabel("Количество студентов")
plt.ylabel("Специальность")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

form_counts = df["Форма обучения"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(form_counts.values, labels=form_counts.index, autopct='%1.1f%%', startangle=90,
        colors=['#FF0000','#002FFF'])
plt.title("Распределение студентов по формам обучения")
plt.tight_layout()
plt.show()