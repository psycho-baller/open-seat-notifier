from search_seats import get_links
from send_email import send

if __name__ == "__main__":
    email_to = 'ramim66809@gmail.com'
    links = get_links('muhammad.tanveer', 'P63ZXfPE')
    if len(links) > 0:
        send(email_to, links)