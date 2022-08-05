import { Box, Flex, Popover, PopoverTrigger, Button, PopoverContent, PopoverArrow, PopoverCloseButton, PopoverHeader, PopoverBody, Spacer, DarkMode, Heading } from "@chakra-ui/react";
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
              <PopoverHeader></PopoverHeader>
              <PopoverBody></PopoverBody>
            </PopoverContent>
          </Popover>
        </Box>
        <Spacer />
        <Box p="4">
          <InfoButton />
        </Box>
      </Flex>
    );
}