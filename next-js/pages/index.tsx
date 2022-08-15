import type { NextPage } from 'next'
import Head from 'next/head'
import ContactForm from '../components/contactForm'
import Footer from '../components/footer'
import { Navbar } from '../components/navbar'
import styles from '../styles/Home.module.css'

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
    <Footer/>
    </div>
  );
}

export default Home
