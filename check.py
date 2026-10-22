import pandas as pd

# Читаем файл
df = pd.read_csv('data/dataset.csv')

# Выводим информацию
print("РАЗМЕР ТАБЛИЦЫ:")
print(f"Строк: {df.shape[0]}")
print(f"Столбцов: {df.shape[1]}")
print("\nСПИСОК СТОЛБЦОВ:")
print(df.columns.tolist())
print("\nТИПЫ ДАННЫХ:")
print(df.dtypes)