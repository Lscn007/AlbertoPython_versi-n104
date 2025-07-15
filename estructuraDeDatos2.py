print("Estructura de Datos2")

# Diccionario que almacena información de empleados
empleados = {
    1001: {"nombre": "Ana", "edad": 28, "departamento": "TI", "salario": 3500},
    1002: {"nombre": "Luis", "edad": 34, "departamento": "Contabilidad", "salario": 4200},
    1003: {"nombre": "Sofía", "edad": 25, "departamento": "Marketing", "salario": 3100},
}

# Mostrar toda la información de los empleados
for id_empleado, datos in empleados.items():
    print(f"ID: {id_empleado}")
    for clave, valor in datos.items():
        print(f"  {clave.capitalize()}: {valor}")
    print()

# Calcular el salario promedio
total_salario = sum(empleado["salario"] for empleado in empleados.values())
promedio_salario = total_salario / len(empleados)
print(f"Salario promedio: {promedio_salario:.2f}")
