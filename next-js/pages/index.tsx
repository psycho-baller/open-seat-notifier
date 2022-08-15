import type { NextPage } from 'next'
import Head from 'next/head'
import ContactForm from '../components/contactForm'
import { Navbar } from '../components/navbar'
import styles from '../styles/Home.module.css'
import { BsGithub, BsLinkedin } from "react-icons/bs";
import { HiOutlineMail } from "react-icons/hi";
import { BiHomeAlt } from "react-icons/bi";
import { HStack } from '@chakra-ui/react'

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>Open Seat Notifier</title>
        <meta
          name="description"
          content="Get Notified when a research study is up for you"
        />
        <link rel="icon" href="https://ucalgary.sona-systems.com/favicon.ico" />
      </Head>
      <Navbar />
      <main className={styles.main}>
        <ContactForm />
      </main>
      <footer className={styles.footer}>
        <HStack spacing={20}>
          <a
            href="https://github.com/psycho-baller/open-seat-notifier"
            target={"_blank"}
            rel={"noopener noreferrer"}
          >
            <BsGithub />
          </a>
          <a
            href="https://www.linkedin.com/in/rami--maalouf/"
            target={"_blank"}
            rel={"noopener noreferrer"}
          >
            <BsLinkedin />
          </a>
          <a
            href="mailto:rami.rami@ucalgary.ca"
            target={"_blank"}
            rel={"noopener noreferrer"}
          >
            <HiOutlineMail />
          </a>
          <a
            href="https://rami-maalouf.vercel.app/"
            target={"_blank"}
            rel={"noopener noreferrer"}
          >
            <BiHomeAlt />
          </a>
        </HStack>
      </footer>
    </div>
  );
}

export default Home
