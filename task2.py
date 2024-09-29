import pandas as pd
import json

# Загрузка данных из JSON-файла
with open('teachers.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Создаем DataFrame из загруженных данных
teachers_df = pd.DataFrame(data)

# Создаем столбец ФИО
teachers_df['ФИО'] = teachers_df['Фамилия'] + ' ' + teachers_df['Имя'] + ' ' + teachers_df['Отчество']

# Выводим только столбец ФИО
print(teachers_df[['ФИО']])
