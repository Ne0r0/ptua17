# Parašykite Python programą, kuri paprašo vartotojo įvesti sveikuosius skaičius, kol vartotojas neįveda 'pabaiga'.
# Šiuos skaičius saugokite aibės duomenų struktūroje (set), kad užtikrintumėte, 
# ,jog visos reikšmės būtų unikalios, o tada atspausdinkite aibę.

# Pavyzdinė įvestis / išvestis:

# Įveskite sveikąjį skaičių (arba 'pabaiga'): 1
# Įveskite sveikąjį skaičių (arba 'pabaiga'): 2
# Įveskite sveikąjį skaičių (arba 'pabaiga'): 1
# Įveskite sveikąjį skaičių (arba 'pabaiga'): 3
# Įveskite sveikąjį skaičių (arba 'pabaiga'): pabaiga
# {1, 2, 3}

unique_numbers = set()

while True:
    user_input = input("Įveskite sveikąjį skaičių arba 'pabaiga': ")
    if user_input.lower() == 'pabaiga':
        break
    try:
        number = int(user_input)
        unique_numbers.add(number)
    except ValueError:
        print("Prašome įvesti sveikąjį skaičių arba 'pabaiga'.")

print("Unikalių skaičių aibė:", unique_numbers)


# Atsakymas:
# unique_numbers = set()

# while True:
#     entry = input("Įveskite sveikąjį skaičių (arba 'pabaiga'): ")
#     if entry == "pabaiga":
#         break
#     unique_numbers.add(int(entry))

# print(unique_numbers)


# # Šios užduoties sprendimas naudojant sąrašą:
# unique_numbers = []

# while True:
#     entry = input("Įveskite sveikąjį skaičių (arba 'pabaiga'): ")
#     if entry == "pabaiga":
#         break
#     number = int(entry)
#     if number not in unique_numbers:
#         unique_numbers.append(number)

# print(unique_numbers)