import {
  Box,
  Flex,
  Popover,
  PopoverTrigger,
  Button,
  PopoverContent,
  PopoverArrow,
  PopoverCloseButton,
  PopoverHeader,
  PopoverBody,
  Spacer,
  DarkMode,
  Heading,
} from "@chakra-ui/react";
import InfoButton from "./infoButton";

export const Navbar = () => {
  return (
    <Flex>
      <Box p="4">
        <Popover>
          <PopoverTrigger>
            <Button>Help</Button>
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
              be read by a script that checks for new research opportunities
              for each user (it's different for each user) and if there is a
              study up, an email will be automatically sent to you.
            </PopoverBody>
          </PopoverContent>
        </Popover>
      </Box>
      <Spacer />
      <Box p="4">
        <InfoButton />
      </Box>
    </Flex>
  );
};
