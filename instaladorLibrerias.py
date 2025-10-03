import os
import subprocess
import sys
from pathlib import Path

def install_requirements(requirements_file: str = "requirements.txt") -> None:
    """
    Instala las dependencias listadas en el archivo requirements.txt usando pip.

    Args:
        requirements_file (str): Nombre del archivo con dependencias.
    """
    file_path = Path(requirements_file)

    if file_path.exists():
        print("📦 Instalando librerías desde requirements.txt...\n")

        # Usamos subprocess en lugar de os.system (más seguro y controlado)
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(file_path)])
            print("\n✅ Instalación completada.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error en la instalación: {e}")
    else:
        print(f"⚠️ No se encontró el archivo '{requirements_file}'.")

if __name__ == "__main__":
    install_requirements()
