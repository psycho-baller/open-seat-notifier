import {
  Popover,
  PopoverTrigger,
  Button,
  PopoverContent,
  PopoverArrow,
  PopoverCloseButton,
  PopoverHeader,
  PopoverBody,
  PopoverFooter,
} from "@chakra-ui/react";
import {motion} from "framer-motion";
import { lClickables } from "../../animations/clickables";


export const HelpButton = () => {
    return(
        <Popover>
          <PopoverTrigger>
            <Button
              as={motion.button}
              initial="initial"
              animate="animate"
              whileHover="hover"
              whileTap="tap"
              variants={lClickables}
            >
              Help
            </Button>
          </PopoverTrigger>
          <PopoverContent>
            <PopoverArrow />
            <PopoverCloseButton />
            <PopoverHeader>How does this work? 🤔</PopoverHeader>
            <PopoverBody>
              After you have submitted your credentials for your{" "}
              <a
                className={`text-lime-300 hover:text-orange-300`}
                href="https://ucalgary.sona-systems.com/"
                target="_blank"
                rel="noopener noreferrer"
              >
                research participation profile
              </a>{" "}
              and your email address that you want to be notified with, your
              data will be securely stored in a remote database which will only
              be read by a script that checks for new research opportunities for
              each user (it&apos;s different for each user) and if there is a
              study up, an email will be automatically sent to you.
            </PopoverBody>
            <PopoverFooter>
              <a
                className={`text-lime-300 hover:text-orange-300`}
                href="https://github.com/psycho-baller/open-seat-notifier/issues"
                rel="noopener noreferrer"
                target="_blank"
              >
                File an issue
              </a>{" "}
              or{" "}
              <a
                className={`text-lime-300 hover:text-orange-300`}
                href="https://www.linkedin.com/in/rami--maalouf/"
                rel="noopener noreferrer"
                target="_blank"
              >
                message me on LinkedIn
              </a>
            </PopoverFooter>
          </PopoverContent>
        </Popover>
    );
}