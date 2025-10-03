# --- Dependencias principales ---
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import config

# --- Inicialización de la app ---
app = Flask(__name__)
app.secret_key = config.SECRET_KEY

# --- Configuración de la base de datos ---
app.config['MYSQL_HOST'] = config.DATABASE['host']
app.config['MYSQL_USER'] = config.DATABASE['user']
app.config['MYSQL_PASSWORD'] = config.DATABASE['password']
app.config['MYSQL_DB'] = config.DATABASE['db']

mysql = MySQL(app)

# --- Rutas principales ---

@app.route('/anyspa')
def inicio():
    """Página de inicio"""
    return render_template('inicio.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Iniciar sesión de usuario"""
    if request.method == 'POST':
        correo = request.form['email']
        contrasena = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT id, nombre_completo, contrasena FROM usuarios WHERE correo = %s", (correo,))
        usuario = cur.fetchone()
        cur.close()

        if usuario and check_password_hash(usuario[2], contrasena):
            # Guardamos sesión
            session['usuario_id'] = usuario[0]
            session['usuario_nombre'] = usuario[1]
            flash(f'Bienvenido, {usuario[1]}', 'success')
            return redirect(url_for('productos'))
        else:
            flash('Correo o contraseña incorrectos', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    """Cerrar sesión de usuario"""
    session.clear()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('login'))


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    """Registro de nuevos usuarios"""
    if request.method == 'POST':
        nombre = request.form['name']
        cedula = request.form['cedula']
        celular = request.form['celular']
        ciudad = request.form['ciudad']
        direccion = request.form['direccion']
        correo = request.form['email']
        contrasena = request.form['password']

        # Encriptamos la contraseña
        contrasena_hash = generate_password_hash(contrasena)

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO usuarios (nombre_completo, cedula, celular, ciudad_residencia, direccion, correo, contrasena)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nombre, cedula, celular, ciudad, direccion, correo, contrasena_hash))
        mysql.connection.commit()
        cur.close()

        flash('Usuario registrado exitosamente. Ya puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    
    return render_template('formulario.html')


@app.route('/productos_citas')
def productos():
    """Vista de productos y citas"""
    if 'usuario_id' not in session:
        flash('Debes iniciar sesión para ver los productos.', 'warning')
        return redirect(url_for('login'))
    
    return render_template('productos_citas.html')


# --- Ejecutar el servidor ---
if __name__ == '__main__':
    app.run(debug=True)
