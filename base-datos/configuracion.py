# configuracion.py

DB_MOTOR = "postgres"  

if DB_MOTOR == "postgres":
    CADENA_CONEXION = "postgresql+psycopg2://user:password@localhost:5434/universidad"
elif DB_MOTOR == "mariadb":
    CADENA_CONEXION = "mysql+pymysql://root:rootpassword@localhost:3308/universidad"
else:
    CADENA_CONEXION = ""