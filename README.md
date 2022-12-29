# Open Seat Notifier

[![wakatime](https://wakatime.com/badge/user/33addb7e-f5e6-470b-a55b-0a8babc62ebb/project/790ea500-6623-4ca0-8d24-29c31f9bb2c5.svg?style=flat-square)](https://wakatime.com/badge/user/33addb7e-f5e6-470b-a55b-0a8babc62ebb/project/790ea500-6623-4ca0-8d24-29c31f9bb2c5)

- V0.1 of this project: https://github.com/psycho-baller/UCalgary-research-participation

## Table of contents

- [Video Demonstration](#video-demonstration)
- [What it does](#what-it-does)
- [Technologies used](#technologies-used-tech-stack)
- [Connect with me](#connect-with-me)
- [Future plans](#future-plans)

# [Video Demonstration](https://youtu.be/25zjPEMxwbk)

https://user-images.githubusercontent.com/81759594/185756962-e055cec3-6163-43dc-8c6f-6c9f81ae1e0e.mp4

[youtube video](https://youtu.be/25zjPEMxwbk)

# What it does

If you're a UCalgary student and taking PSYC 200,201,203? This could be helpful for you.

The purpose of this website is to provide a service to the people who are currently enrolled into [University of Calgary's PSYC intro courses (200, 201, 203)](https://www.ucalgary.ca/pubs/calendar/current/psychology.html), where we suffer from constantly trying to find research participation which is one of the requirements for these courses. So what I decided to do was to create a website where people can submit their credentials here and email so that when there's a new study available, they would be automatically notified, instead of constantly checking the website.

Please [connect with me](#connect-with-me) if you have any good ideas to improve this project in any way.

# Technologies used (tech stack)

- **[NextJs](https://nextjs.org/)** to create a full-stack **[ReactJs](https://reactjs.org/)** Application.
- **[TypeScript](https://www.typescriptlang.org/)** to create a type-safe code.
- **[Python](https://www.python.org/)** to create the backend (scrape the website and send email automatically).
- **[PostgreSQL](https://www.postgresql.org/)** to store the data.
  - 1st time using it.
- **[Prisma](https://www.prisma.io/)** a safer, smoother way to interact with the database, especially with next-js.
  - 1st time using it.
- **[EmailJS](https://www.emailjs.com/)** to send emails automatically.
  - 1st time using it.
- **[Chakra-UI](https://chakra-ui.com/)** to help build the front-end.
- **[tailwindcss](https://tailwindcss.com/)** to help speed up the process of building the front-end.

# Connect with me

if you face any problems or interested in learning how I did this, please feel free to [add an issue](https://github.com/psycho-baller/open-seat-Notifier/issues) or contact me through:

discord: `Rami#2782`

Email: [rami.rami@ucalgary.ca](mailto:rami.rami@ucalgary.ca)

Instagram: [@psycho.baller](https://www.instagram.com/psycho.baller/)

[Linkedin](https://www.linkedin.com/in/rami--maalouf/)

# Future plans

- [X] better email
- [X] Encrypt passwords
- [X] unsubscribe from emails
- [X] change password
- [X] check if the user is already in the database (no dublicates in the database)
- [X] add a loading icon on button when submitting
- [ ] make sure the credentials are valid, if not, they recieve an email abt it
- [ ] change database host
