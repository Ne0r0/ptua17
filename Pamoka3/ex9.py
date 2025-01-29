# Įveskite pirmą skaičių: 7
# Įveskite simbolį (+, -, *, /): *
# Įveskite antrą skaičių: 6
# 7.0 * 6.0 rezultatas yra 42.0

num1 = float(input("Įveskite skaičių: "))
zen = input("Įveskite simbolį (+,-,*,/): ")
num2 = float(input("Įveskite antrą skaičių: "))
atsakymas = None
#paklausti kas yra None. Kokia jo reikšmė?
if zen == "+":
    atsakymas = num1 + num2 
elif zen == "-":
    atsakymas = num1 - num2
elif zen == "*":
    atsakymas = num1 * num2
elif zen == "/":
    atsakymas = num1 / num2
print(f"{num1} {zen} {num2} rezultas yra {atsakymas}")

# first_number = float(input("Įveskite pirmą skaičių: "))
# operator = input("Įveskite simbolį (+, -, *, /): ")
# second_number = float(input("Įveskite antrą skaičių: "))
# result = None

# if operator == "+":
#     result = first_number + second_number
# elif operator == "-":
#     result = first_number - second_number
# elif operator == "*":
#     result = first_number * second_number
# elif operator == "/":
#     result = first_number / second_number

# print(f"{first_number} {operator} {second_number} rezultatas yra {result}")