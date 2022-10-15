import { IconButton } from "@chakra-ui/react";
import { InfoIcon } from "@chakra-ui/icons";
import {
  Popover,
  PopoverTrigger,
  PopoverContent,
  PopoverHeader,
  PopoverBody,
  PopoverFooter,
  PopoverArrow,
  PopoverCloseButton,
  PopoverAnchor,
} from "@chakra-ui/react";
import { rClickables } from "../../animations/clickables";
import { motion } from "framer-motion";



const InfoButton = () => {
  return (
    <Popover>
      <PopoverTrigger>
        <IconButton
          icon={<InfoIcon />}
          aria-label="Info"
          // size="4xs"
          fontSize={25}
          as={motion.button}
          initial="initial"
          animate="animate"
          whileHover="hover"
          whileTap="tap"
          variants={rClickables}
        />
      </PopoverTrigger>
      <PopoverContent>
        <PopoverArrow />
        <PopoverCloseButton />
        <PopoverHeader>What is this? 🤔</PopoverHeader>
        <PopoverBody>
          The purpose of this website is to provide a service to the people who
          are currently enrolled into any of{" "}
          <a
            href="https://www.ucalgary.ca/pubs/calendar/current/psychology.html"
            className={`text-lime-300 hover:text-orange-300`}
            target="_blank"
            rel="noopener noreferrer"
          >
            University of Calgary&apos;s PSYC courses
          </a>
          , especially the intro courses (200, 201, 203) where we suffer from constantly
          trying to find research participation which is one of the requirements
          for these courses. So what I decided to do was to create a website
          where people can submit their credentials here and email so that when
          there&apos;s a new study available, they would be automatically
          notified, instead of constantly checking the website.
        </PopoverBody>
        <PopoverFooter>
          <a
            href="https://github.com/psycho-baller/open-seat-notifier"
            className={`text-lime-300 hover:text-orange-300`}
            target="_blank"
            rel="noopener noreferrer"
          >
            V1.0
          </a>
        </PopoverFooter>
      </PopoverContent>
    </Popover>
  );
};

export default InfoButton;
