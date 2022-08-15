import { useColorMode, IconButton } from "@chakra-ui/react";
import { MoonIcon, SunIcon } from "@chakra-ui/icons";
import { rClickables } from "../../animations/clickables";
import { motion } from "framer-motion";
const DarkMode = () => {
    const { colorMode, toggleColorMode } = useColorMode();
    return (
      <IconButton
        aria-label="Toggle dark mode"
        icon={colorMode === "light" ? <MoonIcon /> : <SunIcon />}
        onClick={toggleColorMode}
        as={motion.button}
        initial="initial"
        animate="animate"
        whileHover="hover"
        whileTap="tap"
        variants={rClickables}
        // variant="ghost"
      />
    );
}

export default DarkMode;