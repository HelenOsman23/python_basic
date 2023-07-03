# Si utilizamos un loop for para recorrer un diccionario, el for va a recorrer las llaves del diccionario y podemos utilizar las llaves para acceder a los valores.

some_dict = {
    "name": "pierina",
    "lastname": "Ramirez",
    "weight": 80,
    "height": 1.70
}

for key in some_dict:
    print(key, some_dict[key])