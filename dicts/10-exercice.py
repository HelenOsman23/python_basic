# Necesitamos saber cuantos artículos únicos compró el cliente y cuantos de cada uno

shopping_cart = ["manzanas","choricillos","yogurt",'alitas de pollo',"jugo de naranja", "confor","mantequilla","choricillos",'alitas de pollo',"jugo de naranja", "confor","mantequilla", "plátanos", "manzanas", "yogurt"]

shopping_counter = {}

for shopping in shopping_cart:
    if shopping in shopping_counter:
        shopping_counter[shopping] += 1
    else:
        shopping_counter[shopping] = 1

print(f"Artículos únicos: {len(shopping_counter)}")

for shopping in shopping_counter:
    print(f"{shopping}: {shopping_counter[shopping]}")

print(f"Articulos totales: {len(shopping_cart)} ")
    
