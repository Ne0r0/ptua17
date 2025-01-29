# Reikia padaryti slot machine tarp 1 - 10
# Pavyzdinė įvestis / išvestis:

# Atspėkite skaičių (1–10): 5
# Per mažas! Bandykite dar kartą.
# Atspėkite skaičių (1–10): 8
# Teisingai! Skaičius yra 8.

import random

# Kompiuteris atsitiktinai parenka skaičių nuo 1 iki 10
secret_number = random.randint(1, 10)

# Pranešame vartotojui apie žaidimo pradžią
print("Sveiki! Aš pasirinkau skaičių nuo 1 iki 10. Pabandykite atspėti!")

# Ciklas, leidžiantis vartotojui spėti, kol jis atspės teisingą skaičių
while True:
    guess = int(input("Įveskite savo spėjimą: "))
    
    if guess < secret_number:
        print("Jūsų spėjimas per mažas. Bandykite vėl.")
    elif guess > secret_number:
        print("Jūsų spėjimas per didelis. Bandykite vėl.")
    else:
        print(f"Teisingai! Aš pasirinkau skaičių {secret_number}.")
        break

# import random

# number = random.randint(1, 10)

# while True:
#     user_guess = int(input("Atspėkite skaičių (1–10): "))
#     if user_guess == number:
#         print(f"Teisingai! Skaičius yra {number}.")
#         break
#     elif user_guess < number:
#         print("Per mažas! Bandykite dar kartą.")
#     else:
#         print("Per didelis! Bandykite dar kartą.")