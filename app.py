import random
import string

def generar_password(longitud=12):
    if longitud < 4:
        raise ValueError("La longitud mínima es 4 caracteres")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password

if __name__ == "__main__":
    print("🔑 Tu contraseña generada es:", generar_password(12))
