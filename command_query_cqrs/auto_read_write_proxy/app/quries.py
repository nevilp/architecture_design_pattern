from db import get_db_conn

def get_users():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM public.user;")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result