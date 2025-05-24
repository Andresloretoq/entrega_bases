from db.connection import get_connection

def crear_cliente(nombre, correo, contraseña):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO clientes (nombre, correo, contraseña)
        VALUES (:1, :2, :3)
    """, (nombre, correo, contraseña))
    conn.commit()
    print("Cliente registrado correctamente.")
