import datetime
import time

seconds = int(input("Введите секунды: "))
for i in range(seconds, 0, -1):
    print(f"Осталось: {i} секунд...")
    time.sleep(1)

print("Время вышло!")