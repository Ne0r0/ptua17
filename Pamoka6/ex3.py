# Įgyvendinkite paprastą žodyną, kuris saugo žodžius ir jų reikšmes. Leiskite vartotojui įvesti žodį ir atspausdinkite jo reikšmę.
# Užduoties instrukcijos:
# Iš anksto užpildykite žodyną keliais žodžiais ir jų reikšmėmis.
# Prašykite vartotojo įvesti žodį, kol ji nuspręs sustoti.
# Atspausdinkite žodžio reikšmę arba klaidą, jei žodyne nėra tokio žodžio.
# Pavyzdinis žodynas galėtų būti toks:


# dictionary = {
#     "obuolys": "vaisius, augantis ant medžių",
#     "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
#     "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",
# }
# Pavyzdinė įvestis / išvestis:


# Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga'): obuolys
# Žodžio obuolys reikšmė: vaisius, augantis ant medžių.
# Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga'): automobilis
# Šio žodžio mūsų žodyne nėra.
# Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga'): pabaiga



# my_dictionary = {
#     "obuolys": "vaisius, augantis ant medžių",
#     "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
#     "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",}

# while True:
#       enter_imput = input("Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga') ")      
#       if enter_imput.lower() == "pabaiga":
#          print("Programa baigta")
#          break
#       if enter_imput in my_dictionary:
#            print(f"Žodžio {enter_imput} reikšmė: {my_dictionary.get(enter_imput)}")
#            break  
#       else:
#            print("Šio žodžio mūsų žodyne nėra")


definitions = {
    "obuolys": "vaisius, augantis ant medžių",
    "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
    "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",}

while True:
      user_imput = input("Please enter word which you are looking for (or 'end') ")      
      if user_imput.lower() == "end":
         print("End of the program")
         break
      if user_imput in definitions:
           print(f"Input {user_imput} meaning: {definitions[user_imput]}")
           break  
      else:
           print("No word found in dictionary")         
         