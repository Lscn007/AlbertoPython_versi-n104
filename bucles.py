print("Ejemplos de bucles")

usuario_correcto = "admin"
clave_correcta = "1234"
intentos = 0

while intentos < 3:
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        break
    else:
        print("Usuario o contraseña incorrectos.")
        intentos += 1

if intentos == 3:
    print("Acceso bloqueado por demasiados intentos.")
