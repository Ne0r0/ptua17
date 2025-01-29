# Tarkime, kad PIN kodas susideda iš 4 atsitiktinių skaitmenų, saugomų kintamajame. 
# Pavadinkime jį stored_pin. Sukurkite ciklą, kuris pereitų per visas galimas kombinacijas, kol rasite saugomą PIN kodą.

# Pavyzdinė išvestis:
# Surastas PIN: 1234


stored_pin = "1234"
pin = 0

while len(str(pin)) < 4 or str(pin) != stored_pin:
    print(pin)
    pin += 1

print(f"Surastas PIN kodas: {stored_pin}")

# stored_pin = "1234"
# for i in range(10000):
#     # Konvertuojame „i“ į string'ą ir rankiniu būdu pridedame 
#     # nulius priekyje, jei to reikia
#     pin = str(i)
#     while len(pin) < 4:
#         pin = "0" + pin

    # if pin == stored_pin:
    #     print(f"Surastas PIN: {pin}")
    #     break