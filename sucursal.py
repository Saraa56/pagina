# app/models/sucursal.py

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
    port=3306,
    user='root',  # Asegúrate de incluir el usuario
    password="12345",
    database="gestion_compras"
    )

def crear_sucursal(nombre, latitud, longitud):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO sucursales (nombre, latitud, longitud)
        VALUES (%s, %s, %s)
    """, (nombre, latitud, longitud))
    
    conn.commit()
    cursor.close()
    conn.close()

def obtener_sucursales():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sucursales")
    sucursales = cursor.fetchall()
    cursor.close()
    conn.close()
    return sucursales
