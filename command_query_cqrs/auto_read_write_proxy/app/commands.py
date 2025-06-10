from db import get_db_conn

def create_user(name:str):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS "user" (id SERIAL PRIMARY KEY, name TEXT);')
    cur.execute('INSERT INTO "user" (name) VALUES (%s);', (name,))
    conn.commit()
    cur.close()
    conn.close()

