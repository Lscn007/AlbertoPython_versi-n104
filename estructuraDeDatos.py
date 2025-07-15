print("Estructura de Datos")

# Diccionario donde cada clave es un curso y su valor es una lista de estudiantes
cursos = {
    "Matemáticas": ["Ana", "Luis", "Pedro"],
    "Historia": ["Ana", "Carlos"],
    "Biología": ["Sofía", "Luis", "Pedro", "Carlos"]
}

# Mostrar todos los cursos y sus estudiantes
for curso, estudiantes in cursos.items():
    print(f"\nCurso: {curso}")
    for estudiante in estudiantes:
        print(f" - {estudiante}")

# Encontrar en qué cursos está inscrito un estudiante específico
def cursos_de_estudiante(nombre):
    inscritos = []
    for curso, estudiantes in cursos.items():
        if nombre in estudiantes:
            inscritos.append(curso)
    return inscritos

# Prueba
nombre = "Luis"
resultado = cursos_de_estudiante(nombre)
print(f"\n{nombre} está inscrito en: {', '.join(resultado)}")
