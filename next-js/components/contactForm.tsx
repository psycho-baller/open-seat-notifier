import {
  FormControl,
  FormLabel,
  FormErrorMessage,
  FormHelperText,
  Input,
  Container,
  Heading,
  Button,
  VStack,
  InputRightElement,
  InputGroup,
} from "@chakra-ui/react";
import { useToast } from "@chakra-ui/react";
import { motion } from "framer-motion";
import { rClickables } from "../animations/clickables";
import { useFormik } from "formik";
import { useState } from "react";
import { useRef } from "react";
import emailjs from "emailjs-com";

interface Email {
  email: string;
}

const ContactForm = () => {
  const form = useRef();
  const toast = useToast();
  const formik = useFormik({
    initialValues: {
      username: "",
      email: "",
      password: "",
    },
    onSubmit: (values) => {
      // alert(JSON.stringify(values, null, 2));
      _onSubmit(values);
    },
  });
  async function _onSubmit(data: any) {
    const email = data.email;
    const username = data.username;
    const password = data.password;
    const res = (await fetch(
      "https://open-seat-finder.vercel.app/api/addUser",
      {
        method: "POST",
        body: JSON.stringify({ email, username, password }),
      }
    )) as Response;
    if (res.status === 201) {
      toast({
        title: "User added successfully",
        description:
          "You will be receiving an email whenever a new study is up",
        status: "success",
        duration: 5000,
        isClosable: true,
      });
      const email_to_send_to = {
        email: email as string,
      };
      emailjs
        .send(
          "open seat finder",
          "osf_t",
          "KLIkJe8rPjR9Cj6Sj",
          //@ts-ignore
          email_to_send_to,
        )
        .then(
          (result) => {
            console.log(result.text);
          },
          (error) => {
            console.log(error.text);
          }
        );
    } else {
      toast({
        title: "Error!",
        description: "Something went wrong, please try again.",
        status: "error",
        duration: 3000,
        isClosable: true,
      });
    }
  }

  const [show, setShow] = useState(false);
  const handleClick = () => setShow(!show);

  return (
    <Container p={4}>
      <Heading p={2}>Open Seat Finder</Heading>

      <form onSubmit={formik.handleSubmit}>
        <FormControl isRequired>
          <FormLabel htmlFor="username">User ID</FormLabel>
          <Input
            placeholder="rick.astley"
            focusBorderColor="green.300"
            id="username"
            name="username"
            type="username"
            variant="filled"
            onChange={formik.handleChange}
            value={formik.values.username}
          />
        </FormControl>
        <FormControl isRequired>
          <FormLabel htmlFor="password">Password</FormLabel>
          <InputGroup>
            <Input
              placeholder="oSIYUo87s"
              focusBorderColor="green.300"
              id="password"
              name="password"
              type={show ? "text" : "password"}
              variant="filled"
              onChange={formik.handleChange}
              value={formik.values.password}
            />
            <InputRightElement width="4.5rem">
              <Button h="1.75rem" size="sm" onClick={handleClick}>
                {show ? "Hide" : "Show"}
              </Button>
            </InputRightElement>
          </InputGroup>
        </FormControl>
        <FormControl isRequired>
          <FormLabel htmlFor="email">Email</FormLabel>
          <Input
            placeholder="rick.astley@gmail.com"
            focusBorderColor="green.300"
            id="email"
            name="email"
            type="email"
            variant="filled"
            onChange={formik.handleChange}
            value={formik.values.email}
          />
        </FormControl>
        <div className="flex justify-center">
          <Button
            as={motion.button}
            initial="initial"
            animate="animate"
            whileHover="hover"
            whileTap="tap"
            variants={rClickables}
            mt={4}
            type="submit"
            className="cursor-pointer"
          >
            <motion.p
              initial="initial"
              animate="animate"
              whileHover="hover"
              whileTap="tap"
              variants={rClickables}
            >
              Notify Me
            </motion.p>
          </Button>
        </div>
      </form>
    </Container>
  );
};

export default ContactForm;
