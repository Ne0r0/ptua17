# Parašykite Python programą, kuri rastų visus pirminius skaičius, esančius vartotojo nurodytame intervale.
# Atspausdinkite pirminių skaičių sąrašą vartotojui.

# Pavyzdinė įvestis / išvestis:

# Įveskite intervalo pradžią: 1
# Įveskite intervalo pabaigą: 13
# Pirminiai skaičiai: [2, 3, 5, 7, 11, 13]

# Prašome vartotojo įvesti intervalo pradžią ir pabaigą
pradzia = int(input("Įveskite intervalo pradžią: "))
pabaiga = int(input("Įveskite intervalo pabaigą: "))
pirminiai_skaiciai = []

for n in range(pradzia, pabaiga + 1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
           pirminiai_skaiciai.append(n)

print("Pirminiai skaičiai:", pirminiai_skaiciai)

# start = int(input("Įveskite intervalo pradžią: "))
# end = int(input("Įveskite intervalo pabaigą: "))
# primes = []

# for num in range(start, end + 1):
#     if num > 1:
#         is_prime = True
        
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
                
#         if is_prime:
#             primes.append(num)

# print("Pirminiai skaičiai:", primes)