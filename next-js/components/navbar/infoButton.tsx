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
const InfoButton = () => {
  return (
    <Popover>
      <PopoverTrigger>
        <IconButton
          icon={<InfoIcon />}
          aria-label="Info"
          // size="4xs"
          fontSize={25}
        />
      </PopoverTrigger>
      <PopoverContent>
        <PopoverArrow />
        <PopoverCloseButton />
        <PopoverHeader>Hey!</PopoverHeader>
        <PopoverBody>
          
        </PopoverBody>
        <PopoverFooter>V2.0</PopoverFooter>
      </PopoverContent>
    </Popover>
  );
};

export default InfoButton;
