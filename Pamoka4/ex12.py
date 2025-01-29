# Įveskite vartojo vardą: admin
# Įveskite slaptažodį: 1234
# Įveskite vartojo vardą: user123
# Įveskite slaptažodį: securepass
# Prisijungimas sėkmingas! Sveiki, user123.


correct_username = "admin"
correct_password = "1234"

while True:
    username = input("Įveskite vartotojo vardą: ")
    password = input("Įveskite slaptažodį: ")
    if username == correct_username and password == correct_password:
        print(f"Sveiki, {username}! Prisijungimas sėkmingas.")
        break
    else:
        print("Neteisingas vartotojo vardas arba slaptažodis. Bandykite dar kartą.")


# username = "user123"
# password = "securepass"

# while True:
#     input_username = input("Įveskite vartojo vardą: ")
#     input_password = input("Įveskite slaptažodį: ")
#     if input_username == username and input_password == password:
#         print(f"Prisijungimas sėkmingas! Sveiki, {username}.")
#         break