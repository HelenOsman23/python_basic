altura = 5  # Altura de la Z

for row in range(altura):
    line = ""
    for col in range(altura):
        if row == 0 or row == (altura - 1) or (col + row) == (altura - 1):
            line += "*"
        else:
            line += " "
    print(line)