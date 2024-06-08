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

import ace_tools as tools; tools.display_dataframe_to_user(name="Таблица оценок учеников", dataframe=df)

df.head()