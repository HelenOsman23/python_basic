# Con listas y diccionarios podemos representar estructuras completas similares a lo 
# que encontramos en el mundo real. por ejemplo, podriamos tener un listado de estudiantes. 
# Cada estudiante es un diccionario con nombre, apellido, curso y una lista de sus calificaciones.
# Ejemplos:

students = [
{
    "name": "Helen",
    "lastname": "Ramírez",
    "course": "Programación",
    "grades": [100,90,95,100],
    "active": False
},
{
    "name": "Osman",
    "lastname": "Ramírez",
    "course": "Viajes espaciales",
    "grades": [90,100,85,],
    "active": True 
}
]

# Ejercicio: Manipular el arreglo de estudiantes para que muestre la siguiente información por cada uno.

# Estudiante: Nombre Apellido
# Curso: Nombre del curso
# Promedio de notas: x
# Estado: Activo/Inactivo

for student in students:
    print("-------------------------------")
    print("Estudiante:", student["name"], student["lastname"])
    print("Curso:", student["course"]) 

    sum = 0
    grades = student["grades"]
    for grade in grades:
        sum += grade

    print("Promedio de notas:", sum/len(grades))  

    if student["active"]:
        print("Estados: Activo")
    else:    
        print("Estado: Inactivo")