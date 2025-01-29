# Ar esate bibliotekos narys? (taip / ne): taip
# Įveskite savo amžių: 14
# Jūs galite skolintis visas knygas.

# Ar esate bibliotekos narys? (taip / ne): taip
# Įveskite savo amžių: 10
# Ar jus lydi suaugęs asmuo? (taip / ne): ne
# Jūs galite skolintis tik vaikų knygas.

# Ar esate bibliotekos narys? (taip / ne): ne
# Jūs negalite skolintis jokių knygų.


# Paprašome vartotojo įvesti informaciją
membership_status = input("Ar esate narys? (taip/ne): ").lower()
age = int(input("Įveskite savo amžių: "))

# Patikriname, ar reikia nurodyti, ar yra lydimas suaugusio asmens
if age < 12:
    accompanied_by_adult = input("Ar jus lydi suaugęs asmuo? (taip/ne): ").lower()
else:
    accompanied_by_adult = "taip"

# Tikriname, ar vartotojas gali skolintis knygas
if membership_status == "taip":
    if age >= 12 or accompanied_by_adult == "taip":
        print("Galite skolintis visas knygas.")
    else:
        print("Galite skolintis tik vaikų knygas.")
else:
    print("Jūs nesate narys, todėl negalite skolintis knygų.")


# membership_status = input("Ar esate bibliotekos narys? (taip / ne): ").lower()

# if membership_status == "taip":
#     age = int(input("Įveskite savo amžių: "))
#     if age >= 12:
#         print("Jūs galite skolintis visas knygas.")
#     else:
#         adult_accompanying = input("Ar jus lydi suaugęs asmuo? (taip / ne): ").lower()
#         if adult_accompanying == "taip":
#             print("Jūs galite skolintis visas knygas.")
#         else:
#             print("Jūs galite skolintis tik vaikų knygas.")
# else:
#     print("Jūs negalite skolintis jokių knygų.")