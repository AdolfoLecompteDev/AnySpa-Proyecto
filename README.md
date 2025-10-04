[README.md](https://github.com/user-attachments/files/22704103/README.md)
# AnySpa - Proyecto

Este es el proyecto **AnySpa**, desarrollado en Python con Flask. El sistema permite la gestión de usuarios, productos y citas, utilizando una arquitectura básica de Flask con plantillas HTML, CSS y JS.

---

## 📂 Estructura del Proyecto

```
AnySpa-Proyecto/
│── app.py # Archivo principal de la aplicación Flask
│── config.py # Configuración del proyecto
│── instaladorLibrerias.py # Script para instalar dependencias
│── requirements.txt # Dependencias del proyecto
│── static/ # Archivos estáticos (CSS, JS, imágenes)
│ ├── formulario.css
│ ├── inicio.css
│ ├── login.css
│ ├── productos_citas.css
│ ├── login.js
│ ├── main.js
│ ├── menu.js
│ └── img/AnySpa.png
│── templates/ # Vistas HTML
│ ├── formulario.html
│ ├── inicio.html
│ ├── login.html
│ └── productos_citas.html
└── .gitignore
```

---

## ⚙️ Instalación y Configuración

1. ### Instalar dependencias
    
Abres la terminal en tu entorno de desarrollo, tienes 2 opciones:

* Usando el script incluido:
    `python instaladorLibrerias.py`

* O directamente desde requirements.txt:
    `pip install -r requirements.txt`

2. ### Ejecutar la aplicación

En la terminal ejecutas el comando de Flask para correr el archivo principal de la aplicación:
`python app.py`

La aplicación quedará disponible en:
http://127.0.0.1:5000

### Rutas accesibles por el momento:
- http://127.0.0.1:5000/anyspa
- http://127.0.0.1:5000/login
- http://127.0.0.1:5000/registro

---

## Notas

* Requiere Python 3.10+.

* El archivo config.py debe incluir la configuración de la base de datos o parámetros de conexión.

* El repositorio incluye un .gitignore básico para excluir archivos innecesarios.
