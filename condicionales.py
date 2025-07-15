print("Ejemplos de condicionales")

def clasificar_edad(edad):
    if edad < 0:
        return "Edad inválida"
    elif edad < 12:
        return "Niño"
    elif edad < 18:
        return "Adolescente"
    elif edad < 60:
        return "Adulto"
    else:
        return "Adulto mayor"

# Prueba
edades = [3, 15, 25, 70, -5]
for edad in edades:
    print(f"Edad: {edad} => {clasificar_edad(edad)}")
