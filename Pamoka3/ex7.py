# Įveskite pirmą skaičių: 5
# Įveskite antrą skaičių: 8.5
# Didesnis skaičius yra 8.5

nr1 = float(input("Įveskite pirmą skaičių: "))
nr2 = float(input("Įveskite antrą skaičių: "))
nr1 = int(nr1)
nr2 = int(nr2)
if nr1 > nr2:
    print(f"Pirmasis skaičius yra didesnis už antrąjį! {nr1}")
elif nr1 == nr2:
    print("Skaičiai yra lygūs!")
else:
    print(f"Antrasis skaičius yra didesnis už pirmąjį! {nr2}")


#     first_number = float(input("Įveskite pirmą skaičių: "))
# second_number = float(input("Įveskite antrą skaičių: "))

# if first_number > second_number:
#     print("Didesnis skaičius yra", first_number)
# elif first_number < second_number:
#     print("Didesnis skaičius yra", second_number)
# else:
#     print("Abu skaičiai yra lygūs.")