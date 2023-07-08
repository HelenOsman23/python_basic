# En el contexto de la programación las funciones son una secuencia de sentencias de código con un nombre.
# Se parecen en algo a las variables en el sentido que son un simple nombre. En el caso de las variables, estas apuntan a un valor, mientras que en el caso de las funciones, apuntan a una serie de sentencias que realizan una tarea específica.

# Podemos definir nuevas funciones para especificar un nombre junto con una secuencia de sentencias que se ejecutan cuando la función es "llamada", "ejecutar" o "invocada"

verses = ["Mano hacia el frente","Puño cerrado","Dedo hacia arriba","Lengua afuera"]

def intro():
  print("¡Atención, compañía!")

def chorus():
  print("Chuchuwa, chuchuwa, chuchuwa wa wa")
  print("Chuchuwa, chuchuwa, chuchuwa wa wa")

def outro():
  print("Lalala lalala lalala la la")
  print("Lalala lalala lalala la la")

for verse in verses:
  intro()
  print(verse)
  if verse != verses[-1]:
    chorus()
  else: 
    outro()
  print("-------")