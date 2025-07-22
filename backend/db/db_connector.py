import psycopg2

def connect_postgres():
    return psycopg2.connect(
        dbname="iot_metrics",
        user="admin",
        password="password",
        host="localhost"
    )
