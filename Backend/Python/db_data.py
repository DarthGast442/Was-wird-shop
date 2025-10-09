import pyodbc
import os
from flask_sqlalchemy import SQLAlchemy

# Options for the connection - future: env-document
user = "DB_ALL"
password = "Christian2025!"
host = "localhost\SQLEXPRESS"
port = ""
dbname = "WasWirdShop"


conn_str = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={host};DATABASE={dbname};UID={user};PWD={password};Encrypt=no"

try:
    conn = pyodbc.connect(conn_str)
    print("Verbindung erfolgreich!")
    conn.close()
except Exception as e:
    print("Fehler beim Verbinden:", e)