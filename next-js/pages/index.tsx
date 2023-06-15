import type { NextPage } from 'next'
import Head from 'next/head'
import ContactForm from '../components/ContactForm'
import Footer from '../components/Footer'
import { Navbar } from '../components/navbar'
import styles from '../styles/Home.module.css'

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Navbar />
      <main className={styles.main}>
        <ContactForm />
      </main>
      <Footer />
    </div>
  );
}

export default Home
