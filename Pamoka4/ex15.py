# Parašykite Python programą, kuri naudoja for ciklą, kad sugeneruotų ir išvestų pirmuosius 10 Fibonacci sekos skaičių.
# Fibonacci sekoje kiekvienas skaičius yra dviejų ankstesnių skaičių suma, pradedant nuo 0 ir 1.
# Fibonacci seka: 0 1 1 2 3 5 8 13 21 34

a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b  

# # Pirmieji du skaičiai Fibonačio sekoje
# a, b = 0, 1  # <-- PASTABA: Vienoje eilutėje galite priskirti kelis kintamuosius!
# print("Fibonacci seka:", end=" ")

# # Mes jau žinome pirmuosius du skaičius, todėl pradedame ciklą nuo trečiojo skaičiaus
# print(a, b, end=" ")

# # PASTABA: _ yra „išmetamasis“ (throwaway) kintamasis. Galite pasidomėti daugiau apie jį ir jo naudojimą!
# for _ in range(8):  # Spausdiname sekančius 8 skaičius, kad iš viso būtų 10 skaičių
#     a, b = b, a + b  # Atnaujiname a ir b reikšmes
#     print(b, end=" ")