from db.connection import get_connection

def agregar_propiedad(id_dueno, direccion, tipo, valor):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO propiedades (id_dueno, direccion, tipo, valor)
        VALUES (:1, :2, :3, :4)
    """, (id_dueno, direccion, tipo, valor))
    conn.commit()

def obtener_propiedades():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, tipo, direccion, valor FROM propiedades")
    return cur.fetchall()

def obtener_propiedad_por_id(prop_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, tipo, direccion, valor FROM propiedades
        WHERE id = :1
    """, (prop_id,))
    return cur.fetchone()

def agregar_a_visitas(id_cliente, id_propiedad):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO visitas (id_cliente, id_propiedad)
        VALUES (:1, :2)
    """, (id_cliente, id_propiedad))
    conn.commit()
