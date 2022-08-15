import {
  Box,
  Flex,
  Spacer,
  HStack,
} from "@chakra-ui/react";
import InfoButton from "./infoButton";
import DarkMode from "./DarkMode";
import { HelpButton } from "./helpButton";

export const Navbar = () => {
  return (
    <Flex>
      <Box p="4">
        <HelpButton/>
      </Box>
      <Spacer />
      <HStack p="4">
          <DarkMode />
          <InfoButton />
      </HStack>
    </Flex>
  );
};
