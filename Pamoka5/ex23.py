# Paprašykite vartotojo įvesti simbolių eilutę. 
# Apskaičiuokite ir atspausdinkite kiekvieno simbolio dažnį eilutėje, naudodami žodyno duomenų struktūrą (dict).

# Pavyzdinė įvestis / išvestis:

# Įveskite simbolių eilutę: labas pasauli
#  : 1
# a: 4
# b: 1
# i: 1
# l: 2
# p: 1
# s: 2
# u: 1

# Paprašome vartotojo įvesti simbolių eilutę
user_string = input("Įveskite simbolių eilutę: ")

# Sukuriame tuščią žodyną simbolių dažniui saugoti
char_frequency = dict()

# Skaičiuojame kiekvieno simbolio dažnį
for char in user_string:
    if char in char_frequency:
        char_frequency[char] += 1  # Padidiname skaičiavimą, jei simbolis jau yra žodyne
    else:
        char_frequency[char] = 1  # Pridedame naują simbolį į žodyną

# Atspausdiname rezultatus
print("Simbolių dažnis eilutėje:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")


# text = input("Įveskite simbolių eilutę: ")
# frequency = {}

# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# for char, freq in sorted(frequency.items()):  # rikiuojame, kad būtų išlaikyta nuosekli tvarka
#     print(f"{char}: {freq}")
