# Parašykite programą, kuri paprašo vartotojo įvesti sveikųjų skaičių sąrašą. 
# Programa turi nustatyti ilgiausią iš eilės einančių skaičių seką sąraše 
# (t. y. skaičiai, kurie seka vienas po kito iš eilės didėdami po 1).
# Atkreipkite dėmesį, kad sąrašas gali būti nesurikiuotas, ir kad pasikartojantys skaičiai neprailgina sekos.

# Pavyzdinė įvestis / išvestis:

# --- 1-as pavyzdys ---
# Įveskite sveikuosius skaičius, atskirtus tarpais: 5 4 2 3 1
# Ilgiausios iš eilės einančių skaičių sekos ilgis yra: 2

# --- 2-as pavyzdys ---
# Įveskite sveikuosius skaičius, atskirtus tarpais: 2 3 4 5 10 1 9 5
# Ilgiausios iš eilės einančių skaičių sekos ilgis yra: 4


def longest_consecutive_sequence(nums):
    # Paverčiame sąrašą į rinkinį
    num_set = set(nums)
    longest_streak = 0

    for num in nums:
        # Tikriname, ar tai yra sekos pradžia
        if num - 1 not in num_set:
            current_streak = 1
            current_num = num

            # Didiname seką
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Atnaujiname ilgiausią seką
            if current_streak > longest_streak:
                longest_streak = current_streak

    return longest_streak

# Vartotojo įvestis
input_nums = input("Įveskite skaičius, atskirtus tarpais: ")
nums = list(map(int, input_nums.split()))
result = longest_consecutive_sequence(nums)
print(f"Ilgiausia iš eilės einančių skaičių seka yra: {result}")


# # Paprašyti vartotojo įvesties
# input_numbers = input("Įveskite sveikuosius skaičius, atskirtus tarpais: ")
# # Konvertuoti įvestį į sveikųjų skaičių sąrašą
# numbers = []
# for num in input_numbers.split():
#     numbers.append(int(num))

# longest_sequence = 1
# current_sequence = 1

# for i in range(1, len(numbers)):
#     if numbers[i] == numbers[i - 1] + 1:
#         current_sequence += 1
#     elif (
#         numbers[i] != numbers[i - 1]
#     ):  # Anuliuoti (reset) seką, jei nėra iš eilės einančio skaičiaus
#         if current_sequence > longest_sequence:
#             longest_sequence = current_sequence
#         current_sequence = 1

# # Galutinis palyginimas, tuo atveju, jeigu ilgiausia seka
# # pasibaigia ties paskutiniu elementu
# if current_sequence > longest_sequence:
#     longest_sequence = current_sequence

# print("Ilgiausios iš eilės einančių skaičių sekos ilgis yra:", longest_sequence)