# Frameworks a usar.
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import config

# Credenciales.
app = Flask(__name__)
app.secret_key = config.SECRET_KEY

# Configuración de la base de datos.
app.config['MYSQL_HOST'] = config.DATABASE['host']
app.config['MYSQL_USER'] = config.DATABASE['user']
app.config['MYSQL_PASSWORD'] = config.DATABASE['password']
app.config['MYSQL_DB'] = config.DATABASE['db']

mysql = MySQL(app)

@app.route('/anyspa')
def inicio():
    return render_template('inicio.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['name']
        cedula = request.form['cedula']
        celular = request.form['celular']
        ciudad = request.form['ciudad']
        direccion = request.form['direccion']
        correo = request.form['email']
        contrasena = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO usuarios (nombre_completo, cedula, celular, ciudad_residencia, direccion, correo, contrasena)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                    (nombre, cedula, celular, ciudad, direccion, correo, contrasena))
        cur.connection.commit()
        cur.close()
        flash('Usuario registrado exitosamente')
        return redirect(url_for('login'))
    
    return render_template('formulario.html')

@app.route('/productos_citas')
def productos():
    return render_template('productos_citas.html')

#Codigo que ejecuta el servidor Flask
if __name__ == '__main__':
    app.run(debug=True)

# Login de la aplicacion
def login():
    if request.method == 'POST':
        correo = request.form['email']
        contrasena = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE correo = %s AND contrasena = %s", (correo, contrasena))
        usuario = cur.fetchone()
        cur.close()

        if usuario:
            # Guardamos la sesión del usuario
            session['usuario'] = usuario[1]  # Ejemplo: nombre completo
            flash('Bienvenido, ' + session['usuario'])
            return redirect(url_for('productos'))
        else:
            flash('Correo o contraseña incorrectos')
            return redirect(url_for('login'))
    
    return render_template('login.html')

# Para cerrar sesion
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Has cerrado sesión correctamente')
    return redirect(url_for('login'))