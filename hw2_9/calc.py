import math

diameter = 580  # мм
height = 50  # мм
steel_density = 7850  # кг/м³
price = 174.28

radius = diameter / 2 / 1000
height = height / 1000
base_area = math.pi * radius**2
volume = base_area * height

weight = volume * steel_density
total_price = weight * price

print("Цена стального круга:", total_price, "грн")

print("Вес стального круга:", weight, "кг")
