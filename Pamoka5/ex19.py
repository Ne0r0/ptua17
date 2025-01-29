# Paprašykite vartotojo įvesti skaičių ir atspausdinkite trikampio dalį iki to skaičiaus (imtinai).
# Kiekvienoje eilutėje turėtų būti skaičiai nuo 1 iki eilutės numerio.

# Pavyzdinė įvestis / išvestis:

# Įveskite trikampio dydį: 4
# 1
# 1 2
# 1 2 3
# 1 2 3 4


size = int(input("Įveskite trikampio dydį: "))

for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # pereiname į naują eilutę

# size = int(input("Įveskite trikampio dydį: "))

# for i in range(1, size + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()  # pereiname į naują eilutę