import MySQLdb

def connect_to_db(host, user, passwd, database):
    return MySQLdb.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=database
    )

def get_raw_dataset(host, user, passwd, database):
    query = """
    SELECT
        e.nombre AS enfermedad,
        GROUP_CONCAT(
            CASE
                WHEN es.sintoma_id IS NOT NULL THEN '1'
                ELSE '0'
            END
            ORDER BY s.id
            SEPARATOR ','
        ) AS sintomas
    FROM
        enfermedades e
    LEFT JOIN
        `sintomas` s ON TRUE
    LEFT JOIN
        `enfermedades_sintomas` es ON e.id = es.enfermedad_id AND s.id = es.sintoma_id
    GROUP BY
        e.id
    ORDER BY
        e.nombre;
    """
    with connect_to_db(host, user, passwd, database) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
    return result

def get_sintomas(host, user, passwd, database):
    query = 'SELECT nombre FROM sintomas;'
    with connect_to_db(host, user, passwd, database) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
    return result



