import calculation

result_z = calculation.calculate_z()
print(f"Результат обчислення z: {result_z}")

hours = int(input("Введіть кількість годин: "))
result_amoeba = calculation.amoeba_count(hours)
print(f"Кількість амеб через {hours} годин: {result_amoeba}")
