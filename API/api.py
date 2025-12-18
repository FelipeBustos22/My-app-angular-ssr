from flask import * 
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

mysql_config = { 
    'host': '172.31.20.5',
    'user': 'admin',
    'password': '*******',
    'database': '*******',
}

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(**mysql_config)
        print('Conexión exitosa')
        return conexion
    except mysql.connector.Error as e:
        print('Error al conectar a MySQL', e)
        return None
    
conectar_mysql()

@app.route('/api', methods=['GET'])
def api():
    conexion = conectar_mysql()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM alumnos')
            registros = cursor.fetchall()
            print(registros)
            cursor.close()
            return jsonify(registros), 200
        except mysql.connector.Error as e:
            print('Error al ejecutar la consulta', e)
            return jsonify('Error al ejecutar la consulta'), 500
        finally:
            conexion.close() 
    else:
        return jsonify('Error al conectar a MySQL'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    #app.run(ssl_context=('/home/ec2-user/selfsigned.crt', '/home/ec2-user/selfsigned.key'), host='0.0.0.0', port=443)
