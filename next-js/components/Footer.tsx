import styles from "../styles/Home.module.css";
import { BsGithub, BsLinkedin } from "react-icons/bs";
import { HiOutlineMail } from "react-icons/hi";
import { BiHomeAlt } from "react-icons/bi";
import { AiFillYoutube } from "react-icons/ai";

// Different ways to add a footer
// https://stackoverflow.com/questions/643879/css-to-make-html-page-footer-stay-at-bottom-of-the-page-with-a-minimum-height-b
export default function Footer() {
  return (
    <section className="fixed bottom-0 flex flex-col w-full">
      <p className="pb-4 text-center ">
        Made with ❤️ by{" "}
        <a
          href="https://ramimaalouf.tech/"
          target={"_blank"}
          rel={"noopener noreferrer"}
          className={`text-lime-300 hover:text-orange-300`}
        >
          Rami
        </a>
      </p>

      <footer className={styles.footer}>
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
          href="https://ramimaalouf.tech/"
          target={"_blank"}
          rel={"noopener noreferrer"}
        >
          <BiHomeAlt />
        </a>
        <a
          href="mailto:rami.rami@ucalgary.ca"
          target={"_blank"}
          rel={"noopener noreferrer"}
        >
          <HiOutlineMail />
        </a>
        <a
          href="https://www.youtube.com/@ramimaalouf"
          target={"_blank"}
          rel={"noopener noreferrer"}
        >
          <AiFillYoutube />
        </a>
      </footer>
    </section>
  );
}
