import psycopg2

DB_CONFIG={
    'dbname':'my_database',
    'user':'postgres',
    'password':'master_password',
    'host':'pgpool',
    'port':5432
}

def get_db_conn():
    return psycopg2.connect(**DB_CONFIG)