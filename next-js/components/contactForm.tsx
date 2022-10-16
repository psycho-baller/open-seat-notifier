import {
  FormControl,
  FormLabel,
  Input,
  Container,
  Heading,
  Button,
  InputRightElement,
  InputGroup,
  Spinner,
} from "@chakra-ui/react";
import { useToast } from "@chakra-ui/react";
import { motion } from "framer-motion";
import { lClickables, rClickables } from "../animations/clickables";
import { useFormik } from "formik";
import { useState } from "react";
import emailjs from "@emailjs/browser";
import { encrypt } from "../utils/encrypt";


const ContactForm = () => {
  const toast = useToast();
  const formik = useFormik({
    initialValues: {
      username: "",
      email: "",
      password: "",
    },
    onSubmit: (values: any) => {
      _onSubmit(values);
    },
  });
  async function _onSubmit(data: any) {
    // setLoading(true);
    const email = data.email;
    const username = data.username;
    const password = encrypt(data.password);
    console.log(email, username, password);

    const res = (await fetch(
      "https://open-seat-notifier.vercel.app/api/addUser",
      {
        method: "POST",
        body: JSON.stringify({ email, username, password }),
      }
    )) as Response;
    if (res.status === 201) {
      toast({
        title: "User added successfully",
        description:
          "You will be receiving a confirmation email shortly!",
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
          email_to_send_to,
          "KLIkJe8rPjR9Cj6Sj"
        )
        .then(
          (result: { text: any; }) => {
            console.log(result.text);
          },
          (error: { text: any; }) => {
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
    // setLoading(false);
  }

  const [show, setShow] = useState(false);
  const handleClick = () => setShow(!show);
  // const [loading, setLoading] = useState(false);


  return (
    <Container p={3}>
      <Heading py={2}>Open Seat Notifier</Heading>

      <form onSubmit={formik.handleSubmit}>
        <FormControl isRequired py={2}>
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
        <FormControl isRequired py={2}>
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
        <FormControl isRequired py={2}>
          <FormLabel htmlFor="email">Email</FormLabel>
          <Input
            placeholder="rick.astley@ucalgary.ca"
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
              variants={lClickables}
            >
              Notify Me
            </motion.p>
            {/* {!{ loading } && <Spinner />} */}
          </Button>
        </div>
      </form>
    </Container>
  );
};

export default ContactForm;
