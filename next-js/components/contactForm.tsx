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
} from "@chakra-ui/react";
import { useForm } from "react-hook-form";
import { useToast } from "@chakra-ui/react";
import { motion } from "framer-motion";
import { rClickables } from "../animations/clickables";
import { useFormik } from "formik";


const ContactForm = () => {
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
  // const {
  //   handleSubmit,
  //   register,
  //   formState: { errors, isSubmitting, isDirty },
  // } = useForm({ defaultValues: { username: "", password: "", email: "" } });
  async function _onSubmit(data: any) {
    const email = data.email
    const username = data.username
    const password = data.password
    const res = (await fetch(
          "https://open-seat-finder.vercel.app/api/addUser",
          {
            method: "POST",
            body: JSON.stringify({ email, username, password }),
          }
        )) as Response;
        if (res.status === 201) {
      toast({
        title:"User added successfully",
        description:"You will be receiving an email whenever a new study is up",
        status: "success",
        duration: 5000,
        isClosable: true,
      });
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
    //   alert(JSON.stringify({ name, email, message }));
    //   resolve();
    //   }, 1000);
    // });

  return (
    <Container p={4}>
      <Heading p={2}>Open Seat Finder</Heading>

      <form onSubmit={formik.handleSubmit}>
        <FormControl isRequired>
          <FormLabel htmlFor="username">Username</FormLabel>
          <Input
            focusBorderColor="yellow.200"
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
          <Input
            focusBorderColor="yellow.200"
            id="password"
            name="password"
            type="password"
            variant="filled"
            onChange={formik.handleChange}
            value={formik.values.password}
          />
        </FormControl>
        <FormControl isRequired>
          <FormLabel htmlFor="email">Email</FormLabel>
          <Input
            focusBorderColor="yellow.200"
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
            Submit
          </motion.p>
        </Button>
        </div>
      </form>
    </Container>
  );
};

export default ContactForm;