import pandas as pd
import random
from datetime import datetime, timedelta

# Generate random student names
names = ["Алексей", "Борис", "Виктория", "Галина", "Дмитрий", "Елена", "Игорь", "Ксения", "Мария", "Никита"]

# Generate subjects
subjects = ["Математика", "Русский язык", "Физика", "История", "Биология"]

# Generate random dates
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(20)]

# Generate data
data = []
for name in names:
    num_grades = random.randint(5, 10)
    for _ in range(num_grades):
        subject = random.choice(subjects)
        date = random.choice(dates)
        grade = random.randint(2, 5)
        data.append([name, subject, date.strftime('%Y-%m-%d'), grade])

# Create DataFrame
df = pd.DataFrame(data, columns=["Имя", "Предмет", "Дата", "Оценка"])



print(df.head())


mean_grades = df.groupby('Предмет')['Оценка'].mean()

median_grades = df.groupby('Предмет')['Оценка'].median()

std_dev_grades = df.groupby('Предмет')['Оценка'].std()

statistics = pd.DataFrame({
    'Средняя оценка': mean_grades,
    'Медианная оценка': median_grades,
    'Стандартное отклонение': std_dev_grades
})
print(statistics)

q1_grades = df[df['Предмет'] == 'Математика']['Оценка'].quantile(0.25)
print(f'Q1  Математика - {q1_grades}')
q3_grades = df[df['Предмет'] == 'Математика']['Оценка'].quantile(0.75)
print(f'Q3 Математика - {q3_grades}')

iqr_grades = q3_grades - q1_grades
print(f'IQR Математика - {iqr_grades}')




