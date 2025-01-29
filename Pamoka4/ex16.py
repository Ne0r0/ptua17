# Sukurkite programą, leidžiančią vartotojui po vieną įvesti skaičius iki tol, kol jis įves pabaiga.
# Tada atspausdinkite skaičių sąrašą ir apskaičiuotą jų vidurkį.

# Pavyzdinė įvestis / išvestis:

# Įveskite skaičių (arba įveskite 'pabaiga'): 4
# Įveskite skaičių (arba įveskite 'pabaiga'): 5
# Įveskite skaičių (arba įveskite 'pabaiga'): 6
# Įveskite skaičių (arba įveskite 'pabaiga'): 7
# Įveskite skaičių (arba įveskite 'pabaiga'): pabaiga
# Skaičiai: [4.0, 5.0, 6.0, 7.0]
# Vidurkis: 5.5


numbers = []

while True:
    user_input = input("Įveskite skaičių (arba 'pabaiga' norėdami baigti): ")
    
    if user_input == "pabaiga":
        break
    numbers.append(float(user_input))

if numbers:
    print(f"Įvesti skaičiai: {numbers}")
    print(f"Vidurkis: {sum(numbers) / len(numbers)}")
else:
    print("Jūs neįvedėte nei vieno skaičiaus.")


# # Sukurti tuščią sąrašą, skirtą skaičiams saugoti
# numbers = []

# while True:
#     # Paprašyti vartotojo įvesti skaičių arba „pabaiga“, kad užbaigtų
#     entry = input("Įveskite skaičių (arba įveskite 'pabaiga'): ")
#     if entry == "pabaiga":
#         break
#     # Konvertuoti įvestį į float tipo skaičių ir pridėti jį į sąrašą
#     numbers.append(float(entry))

# # Patikrinti, ar sąrašas nėra tuščias prieš apskaičiuojant vidurkį
# if len(numbers) > 0:
#     total = sum(numbers)
#     average = total / len(numbers)
# else:
#     average = 0

# # Atspausdinti skaičių sąrašą ir vidurkį
# print(f"Skaičiai: {numbers}")
# print(f"Vidurkis: {average}")