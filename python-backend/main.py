from search_seats import get_links, get_details, close_driver
from send_email import send_sub_email
from queries import connect, get_all_data, close_connection, add_to_notified
import psycopg2
#!/usr/bin/python
from config import config
from decrypt import decrypt
# To activate the venv, run the following command in bash:
# source open-seat-venv/Scripts/activate


def main():

    results  = get_all_data()
    for result in results:
        email = result[0]
        notified = result[1] if result[1] else []
        username = result[2]
        password = result[3]
        password = decrypt(password)
        if email == "ramim66809@gmail.com" or email == "Abitibebu123@gmail.com" or username == "annni13" or username == "Anileah.berger" or username == "simra.naveed" or username == "grace.pele":
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
                add_to_notified(email, link)
        if links_to_notify:
            send_sub_email(email, links_to_notify)




if __name__ == "__main__":
    # Connect to the Postgres database
    connect()
    main()
    close_connection()
