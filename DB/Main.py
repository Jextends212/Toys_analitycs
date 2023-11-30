import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import json

try:
    # Cargamos nuestras credenciales de nuestra BD:

    with open('config.json') as f:
        config = json.load(f)

    # Conectamos a nuestra BD de MySQL:

    db_connection = mysql.connector.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['database']
    )
    

    # Creamos un motor SQLAlchemy para la conexión con MySQL:

    engine = create_engine(f"mysql+mysqlconnector://{config['mysql']['user']}:{config['mysql']['password']}@{config['mysql']['host']}/{config['mysql']['database']}")

    #Verificamos si existe la conexion:

    if db_connection.is_connected():
        cursor = db_connection.cursor()

        # Con SQL obtenemos los nombres de las columnas de la BD:

        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'sales_samples'")
        column_names = [column[0] for column in cursor.fetchall()]

        # Realizamos la consulta SQL para obtener los datos:
        cursor.execute("SELECT * FROM sales_samples")
        result = cursor.fetchall()

        # Guardamos los datos en un DataFrame de PANDAS :)
        
        df = pd.DataFrame(result, columns=column_names)

        # Guardamos los datos en un archivo de Excel -->
        df.to_excel("sales.xlsx", index=False)
        print("Datos exportados a sales.xlsx")
        

except Exception as e:
    print("Error:", e)

finally:
    #Cerramos la conexion con nuestra BD:
    # 
    if db_connection.is_connected():
        db_connection.close()
