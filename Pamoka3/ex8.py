# Įveskite savo vardą: Jonas
# Įveskite savo pavardę: Jonaitis
# Įveskite savo amžių: 22
# Jonas Jonaitis, jums leidžiama patekti į kazino.

vardas = input("Įveskite savo vardą: ")
pavarde = input("Įveskite savo pavardę: ")
amzius = int(input("Įveskite savo amžių: "))
riba = 21

if amzius >= riba:
    print(f"{vardas} {pavarde}, jums leidžiama patekti į kazino.")
elif amzius < 21:
    print(f"{vardas} {pavarde}, esate per jaunas!")


# # Gauti vartotojo vardą, pavardę ir amžių
# name = input("Įveskite savo vardą: ")
# surname = input("Įveskite savo pavardę: ")
# age = int(input("Įveskite savo amžių: "))

# # Patikrinti, ar vartotojui leidžiama patekti į kazino
# if age >= 21:
#     print(f"{name} {surname}, jums leidžiama patekti į kazino.")
# else:
#     print(f"{name} {surname}, jums neleidžiama patekti į kazino.")