meters = float(input("Введите количество метров: "))
centimeters = meters * 100
decimeters = meters * 10
millimeters = meters * 1000
miles = meters / 1609.34


print(f"{meters} метров = {centimeters} сантиметров")
print(f"{meters} метров = {decimeters} дециметров")
print(f"{meters} метров = {millimeters} миллиметров")
print(f"{meters} метров = {miles} миль")
