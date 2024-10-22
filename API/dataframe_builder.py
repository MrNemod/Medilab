import pandas as pd
import mysql_operations as de

#Informacion de la bd
bd = {
    'host' : 'localhost',
    'user' : 'root',
    'passwd' : 'Luis3334',
    'database' : 'sistema_enfermedades'
}

# Obtener los datos
data = de.get_raw_dataset(bd['host'], bd['user'], bd['passwd'], bd['database'])
sintomas = de.get_sintomas(bd['host'], bd['user'], bd['passwd'], bd['database'])

# Convertir los datos
enfermedades = [item[0] for item in data]
valores = [list(map(int, item[1].split(','))) for item in data]

df = pd.DataFrame(valores, index=enfermedades, columns=sintomas)
