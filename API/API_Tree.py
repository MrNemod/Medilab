
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import Tree

app = Flask(__name__)
CORS(app)

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Luis3334',
    'database': 'sistema_enfermedades'
}

def connect_db():
    return mysql.connector.connect(**db_config)

@app.route('/symptoms', methods=['GET'])
def read_syntoms():
    try:
        connection = connect_db()
        cursor = connection.cursor(dictionary=True)
        query = 'SELECT * FROM sintomas'

        cursor.execute(query)
        records = cursor.fetchall()

        cursor.close()
        connection.close()
        return jsonify(records), 200
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

@app.route('/prediction', methods=['POST'])
def show_prediction():
    try:
        symptoms_list = request.json
        print("Síntomas recibidos:", symptoms_list)

        prediction_result = Tree.prediccion(symptoms_list)

        return jsonify({"prediction": prediction_result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/medicine', methods=['POST'])
def show_medicament():
    try:
        predicted_disease = request.json.get('predicted_disease')
        print("Enfermedad predicha:", predicted_disease)

        connection = connect_db()
        cursor = connection.cursor(dictionary=True)
        query = '''
            SELECT medicinas_enfermedades.id_medicamento, medicinas.nombre, medicinas.stock
            FROM medicinas_enfermedades
            JOIN medicinas ON medicinas_enfermedades.id_medicamento = medicinas.id
            JOIN enfermedades ON medicinas_enfermedades.id_enfermedad = enfermedades.id
            WHERE enfermedades.nombre = %s
        '''
        cursor.execute(query, (predicted_disease,))
        records = cursor.fetchall()

        cursor.close()
        connection.close()

        print("Lista de medicamentos:", records)

        return jsonify(records), 200

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)