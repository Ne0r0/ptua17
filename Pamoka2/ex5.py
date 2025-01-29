# Įveskite pradinę sumą: 1000
# Įveskite palūkanų normą (%): 5
# Įveskite laiką (metais): 3
# Paprastosios palūkanos yra 150.0


suma = float(input("Įveskite pradinę sumą: "))
norma = float(input("Įveskite palūkanų normą (%): "))
metai = float(input("Įveskite laiką (metais): "))
# suma = float(suma)
# norma = float(norma)
# metai = float(metai)
print(f"suma: {suma}, norma: {norma}, metai: {metai}")
rezultatas = (metai * norma * suma) / 100
print(rezultatas)
print(f"Paprastosios palūkanos yra {rezultatas}")



#  P = float(input("Įveskite pradinę sumą: "))
#  N = float(input("Įveskite palūkanų normą (%): "))
#  L = float(input("Įveskite laiką (metais): "))
#  PP = (P * N * L) / 100

# print("Paprastosios palūkanos yra", PP)