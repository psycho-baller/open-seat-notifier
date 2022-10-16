from send_email import send_sub_email, send_unsub_email
#!/usr/bin/python
from decrypt import decrypt
import psycopg2
from config import config
# To activate the venv, run the following command in bash:
# source open-seat-venv/Scripts/activate
cur = None
conn = None

def main(conn, cur):
    from queries import get_all_data, close_connection, add_to_notified, delete_user
    from search_seats import get_links, get_details, close_driver

    results  = get_all_data(cur)
    for result in results:
        email = result[0]
        notified = result[1] if result[1] else []
        username = result[2]
        password = result[3]
        password = decrypt(password)

        
        links = get_links(username, password)
        if "delete" in links:
            delete_user(cur, username)
            send_unsub_email(email)
            continue
        
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
                add_to_notified(cur, conn, email, link)
        if links_to_notify:
            send_sub_email(email, links_to_notify)
    close_connection(conn, cur)
    close_driver()


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
        print('version:', db_version)

        return conn, cur

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    #         print('Database connection closed.')

# def get_cur():
#     return cur

def get_conn():
    return conn

if __name__ == "__main__":
    # Connect to the Postgres database
    conn, cur = connect()
    main(conn, cur)
