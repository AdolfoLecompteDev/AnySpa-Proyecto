import os

# Verifica si requirements.txt existe
if os.path.exists("requirements.txt"):
    print("📦 Instalando librerías desde requirements.txt...\n")
    os.system("py -m pip install -r requirements.txt")
    print("\n✅ Instalación completada.")
else:
    print("⚠️ No se encontró el archivo 'requirements.txt'.")
