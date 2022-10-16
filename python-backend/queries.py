from main import get_conn

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
add_to_notified_query = 'UPDATE public.main WHERE email = %s SET notified_studies = array_append(notified_studies, %s);'

add_user_query = 'INSERT INTO public.main (email, username, password) VALUES (%s, %s, %s);'
get_all_data_query = '''SELECT * FROM public.main
            ORDER BY id ASC; '''
delete_user_query = 'DELETE FROM public.main WHERE username = %s;'
get_email_query = 'SELECT email FROM public.main WHERE username = %s;'
remove_duplicates = '''

'''

def get_all_data(cur):
    cur.execute(get_all_data_query)
    return cur.fetchall()

def close_connection(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

def add_to_notified(cur, conn, email, link):
    cur.execute(add_to_notified_query, (link, email))
    conn.commit()

def delete_user(cur, username):
    cur.execute(delete_user_query, (username,))

# def get_email(cur, username):
#     cur.execute(get_email_query, (username,))
#     return cur.fetchone()[0]
