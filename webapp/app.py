from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configuración de conexión
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'veterinaria'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    nombre_mascota = request.form['nombre_mascota']
    especie = request.form['especie']
    raza = request.form['raza']
    edad = request.form['edad']
    nombre_duenio = request.form['nombre_duenio']

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        query = '''
            INSERT INTO mascotas (nombre_mascota, especie, raza, edad, nombre_duenio)
            VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (nombre_mascota, especie, raza, edad, nombre_duenio))
        conn.commit()
        cursor.close()
        conn.close()
        return f"Mascota registrada exitosamente: {nombre_mascota} ({especie}, {raza}, {edad} años) - Dueño: {nombre_duenio}"
    except mysql.connector.Error as err:
        return f"Error al registrar: {err}"

if __name__ == '__main__':
    app.run(debug=True)
