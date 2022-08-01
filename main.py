from search_seats import get_links
from send_email import send
import psycopg2
#!/usr/bin/python
from config import config


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
        
        """ Commands """
        add_to_notified = 'UPDATE public.main SET "notified-studies" = array_append("notified-studies", %s);'
        get_all_data = '''SELECT * FROM public.main
            ORDER BY id ASC; '''

        
        """ Playgroud"""

        cur.execute(get_all_data)
            
        links_to_notify = []
        results  = cur.fetchall()
        for result in results:
            email = result[0]
            notified = result[2] if result[2] else []
            new = result[3]
            username = result[4]
            password = result[5]
            # print(email,notified, username, password)
            links = get_links(username, password)
            # add links to notified list
            for link in links:
                if link not in notified:
                    links_to_notify.append(link)
                    cur.execute(add_to_notified, (link,))
            if links_to_notify:
                send(email, links_to_notify)
        
        

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
    
    # email_to = 'ramim66809@gmail.com'
    # links = get_links('muhammad.tanveer', 'P63ZXfPE')
    # if len(links) > 0:
    #     send(email_to, links)


if __name__ == "__main__":
    main()