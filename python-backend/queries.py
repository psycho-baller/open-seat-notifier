import psycopg2
#!/usr/bin/python
from config import config
conn = None
cur = None

""" Create Table """
create_table = '''
CREATE TABLE public.main
(
    email character varying NOT NULL,
    notified_studies character varying[] DEFAULT array[]::varchar[],
    username character varying NOT NULL,
    password character varying NOT NULL
);

ALTER TABLE IF EXISTS public.main
    OWNER to lzpgnnepunoeer;'''

""" Commands """
add_to_notified = 'UPDATE public.main WHERE email = %s SET notified_studies = array_append(notified_studies, %s);'

add_user = 'INSERT INTO public.main (email, username, password) VALUES (%s, %s, %s);'
get_all_data = '''SELECT * FROM public.main WHERE id > 70
            ORDER BY id ASC; '''
delete_user = 'DELETE FROM public.main WHERE username = %s;'
get_email = 'SELECT email FROM public.main WHERE username = %s;'
remove_duplicates = '''

'''

def connect():
    """ Connect to the PostgreSQL database server """
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

    # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
 
       
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            
def get_all_data():
    
    cur.execute(get_all_data)
    return cur.fetchall()

def close_connection():
    conn.commit()
    cur.close()
    conn.close()
    
def add_to_notified(email, link):
    cur.execute(add_to_notified, (link, email))
    conn.commit()
    
def delete_user(username):
    cur.execute(delete_user, (username,))

def get_email(username):
    cur.execute(get_email, (username,))
    return cur.fetchone()[0]