import pandas as pd
import random
from datetime import datetime, timedelta

# Определение количества записей
num_records = 1000000

# Определение регионов
regions = ['Москва', 'Красноярский край', 'Волгоградская область', 'Республика Татарстан', 'Санкт-Петербург']

# Определение курсов
courses = ['1 курс', '2 курс', '3 курс', '4 курс']

# Определение университетов
universities = ['ВШЭ', 'СФУ', 'ВолГУ', 'КФУ', 'ИТМО']

# Генерация данных
data = {
    'id': range(1, num_records + 1),
    'ФИО': ['Имя' + str(i) for i in range(num_records)],
    'Дата рождения': [datetime.now() - timedelta(days=random.randint(18*365, 60*365)) for _ in range(num_records)],
    'номер телефона': ['+7' + str(random.randint(9000000000, 9999999999)) for _ in range(num_records)],
    'регион': [random.choice(regions) for _ in range(num_records)],
    'дата регистрации': [datetime.now() - timedelta(days=random.randint(0, 3*365)) for _ in range(num_records)],
    'курс обучения': [random.choice(courses) for _ in range(num_records)],
    'вуз': [random.choice(universities) for _ in range(num_records)]
}

df = pd.DataFrame(data)
df['Дата рождения'] = pd.to_datetime(df['Дата рождения'])
df['дата регистрации'] = pd.to_datetime(df['дата регистрации'])

# Расчет количества регистраций по регионам
registrations_by_region = df['регион'].value_counts()

# Расчет количества регистраций за определенный период времени
start_date = datetime.now() - timedelta(days=365)  # год назад
end_date = datetime.now()  # сегодня
registrations_by_time_period = df[(df['дата регистрации'] >= start_date) & (df['дата регистрации'] <= end_date)].shape[0]

# Отображение пользователей в возрасте от 18 до 35 лет
current_year = datetime.now().year
users_18_35 = df[(df['Дата рождения'].dt.year >= current_year - 35) & (df['Дата рождения'].dt.year <= current_year - 18)]

# Вывод количества регистраций по регионам
print("Количество регистраций по регионам:")
print(registrations_by_region)

# Вывод количества регистраций за определенный период времени
print("\nКоличество регистраций за последний год:")
print(registrations_by_time_period)

# Вывод пользователей в возрасте от 18 до 35 лет
print("\nПользователи в возрасте от 18 до 35 лет:")
print(users_18_35)
