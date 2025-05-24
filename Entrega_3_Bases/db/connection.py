import cx_Oracle

def get_connection():
    try:
        dsn = cx_Oracle.makedsn(
            host="10.34.1.33",
            port=1521,
            service_name="LABORATORIO"  # PDB que debes usar
        )

        connection = cx_Oracle.connect(
            user="is213808",
            password="vw6UONGYrHNdsAV",
            dsn=dsn
        )

        print(" Conexión exitosa a Oracle. ")
        return connection

    except cx_Oracle.DatabaseError as e:
        print(" Error al conectar a Oracle: ", e)
        return None

def obtener_propiedades():
    conn = get_connection()
    if conn is None:
        return []
    cur = conn.cursor()
    cur.execute("SELECT id, tipo, direccion, valor FROM propiedades")
    return cur.fetchall()
