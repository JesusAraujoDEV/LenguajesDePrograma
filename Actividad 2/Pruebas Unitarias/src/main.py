def suma(x,y):
    return x+y
def es_mayor(x,y):
    return x>y
def login(usuario,contraseña):
    return usuario == "admin" and contraseña == "1234"

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

