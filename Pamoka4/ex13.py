# Leiskite vartotojui įvesti 10 sveikųjų skaičių, tada atspausdinkite šių skaičių sumą ir vidurkį.
# Įveskite sveikąjį skaičių 1: 5
# Įveskite sveikąjį skaičių 2: 3
# ...
# Įveskite sveikąjį skaičių 10: 2
# Suma: 45, Vidurkis: 4.5

numbers = []
print("Įveskite 10 sveikųjų skaičių: ")

for i in range(10):
    number = int(input(f"Skaičius {i + 1}: "))
    numbers.append(number)

total = sum(numbers)
average = total / 10

print(f"Skaičių suma: {total}")
print(f"Skaičių vidurkis: {average}")

# total_sum = 0

# for i in range(10):
#     number = int(input(f"Įveskite sveikąjį skaičių {i + 1}: "))
#     total_sum += number
    
# average = total_sum / 10
# print(f"Suma: {total_sum}, Vidurkis: {average}")