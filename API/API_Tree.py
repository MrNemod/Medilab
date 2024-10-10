
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Luis3334',
    'database': 'sistema_enfermedades'
}

def connect_db():
    return mysql.connector.connect(**db_config)

@app.route('/diseases', methods=['GET'])
def read_diseases():
    try:
        connection = connect_db()
        cursor = connection.cursor(dictionary=True)
        query = 'SELECT * FROM enfermedades'

        cursor.execute(query)
        records = cursor.fetchall()

        cursor.close()
        connection.close()
        return jsonify(records), 200
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

@app.route('/medicine')
def read_medicine():
    try:
        connection = connect_db()
        cursor = connection.cursor(dictionary=True)
        query = 'SELECT * FROM medicinas'

        cursor.execute(query)
        records = cursor.fetchall()

        cursor.close()
        connection.close()
        return jsonify(records), 200
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=500)