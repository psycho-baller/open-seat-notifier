from search_seats import get_links, get_details, close_driver
from send_email import send
import psycopg2
#!/usr/bin/python
from config import config
from decrypt import decrypt
# To activate the venv, run the following command in bash:
# source open-seat-venv/Scripts/activate

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
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
        
        """ Create Table """
        create_table='''
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
        add_to_notified = 'UPDATE public.main SET notified_studies = array_append(notified_studies, %s);'
        get_all_data = '''SELECT * FROM public.main
            ORDER BY id ASC; '''
        add_user = 'INSERT INTO public.main (email, username, password) VALUES (%s, %s, %s);'


        """ Playgroud"""
        cur.execute(get_all_data)

        results  = cur.fetchall()
        for result in results:
            email = result[0]
            notified = result[1] if result[1] else []
            username = result[2]
            password = result[3]
            password = decrypt(password)
            if email == "ramim66809@gmail.com" or email == "Abitibebu123@gmail.com" or username == "annni13":
                continue
            # print( email,notified,username,password)
            
            links = get_links(username, password)
            
            links_to_notify = []

            # add links to notified list
            for link in links:
                if link not in notified:
                    # Make a new hashMap for the new link
                    data = {}
                    data["link"] = link
                    title, description, credits_, duration, location = get_details(link)
                    data["title"] = title
                    data["description"] = description
                    data["credits"] = credits_
                    data["duration"] = duration
                    data["location"] = location
                    # After adding the details that we wanna show in the email,
                    # we add it to the list that we wanna send to the email
                    links_to_notify.append(data)
                    cur.execute(add_to_notified, (link,))
            if links_to_notify:
                send(email, links_to_notify)
        close_driver()


	    # close the communication with the PostgreSQL
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
def main():
    # Connect to the Postgres database
    connect()



if __name__ == "__main__":
    main()
