verses = ["Mano hacia el frente","Puño cerrado","Dedo hacia arriba","Lengua afuera"]
print(verses[-1])

for verse in verses:
  if verse != verses[-1]:
    print("Todavía no llegamos")
  else:
    print("Llegamos al final")
    