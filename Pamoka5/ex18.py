# Pradėkite sukurdami sąrašą, pavadintą shopping_list, kuriame yra šie elementai: 'pienas', 'kiaušiniai', 'duona', 'sviestas'.
# Pasirodo, kad suklydote su pirkinių sąrašu, ir dabar turite tai ištaisyti.
# Pirmiausia atspausdinkite sąrašą ir jo pirmąjį elementą.
# Pakeiskite 'duona' į 'bananas' (tarkime, kad nežinote, kur yra 'duona' sąraše, ir pirmiausia turite rasti 'duona' indeksą).
# Įterpkite 'obuolys' į sąrašo pradžią.
# Pridėkite prekes 'miltai' ir 'cukrus', kurias pamiršote pridėti anksčiau.
# Atspausdinkite sąrašo dalį, kurioje yra tik 'kiaušiniai' ir 'bananas'. Naudokite sąrašo karpymą.
# Atspausdinkite sąrašą po kiekvieno žingsnio.

# Norimas rezultatas:
# ['pienas', 'kiaušiniai', 'duona', 'sviestas']
# pienas
# ['pienas', 'kiaušiniai', 'bananas', 'sviestas']
# ['obuolys', 'pienas', 'kiaušiniai', 'bananas', 'sviestas']
# ['obuolys', 'pienas', 'kiaušiniai', 'bananas', 'sviestas', 'miltai', 'cukrus']
# ['kiaušiniai', 'bananas']

shopping_list = ["pienas", "kiaušiniai", "duona", "sviestas"]

print(shopping_list)

print(str(shopping_list[0]))

shopping_list.remove("duona")
shopping_list.insert(2, "bananas")
print(shopping_list)

shopping_list.insert(0, "obuolys")
print(shopping_list)

more_list = ["miltai", "cukrus"]
shopping_list.extend(more_list)
print(shopping_list)

print(shopping_list[2:4])


# shopping_list = ["pienas", "kiaušiniai", "duona", "sviestas"]
# print(shopping_list)
# print(shopping_list[0])

# shopping_list[shopping_list.index("duona")] = "bananas"
# print(shopping_list)

# shopping_list.insert(0, "obuolys")
# print(shopping_list)

# shopping_list.extend(["miltai", "cukrus"])
# print(shopping_list)

# print(shopping_list[2:4])