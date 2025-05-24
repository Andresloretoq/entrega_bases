from db.connection import get_connection
from datetime import datetime

def rentar_propiedad(id_cliente, id_propiedad):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO rentas (id_cliente, id_propiedad, fecha, metodo_pago)
        VALUES (:1, :2, :3, 'efectivo')
    """, (id_cliente, id_propiedad, datetime.now()))
    conn.commit()
    print("Propiedad rentada exitosamente.")
