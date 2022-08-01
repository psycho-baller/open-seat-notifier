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


const ContactForm = () => {
  const toast = useToast();
  const {
    handleSubmit,
    register,
    formState: { errors, isSubmitting, isDirty },
  } = useForm({ defaultValues: { username: "", password: "", email: "" } });
  async function onSubmit(data: any) {
    console.log("clickeda")
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
        title: "Success!",
        description: "Thank you for contacting us!",
        status: "success",
        duration: 3000,
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
      <Heading p={2}>Plz lemme hack u</Heading>

      <form action="" onSubmit={handleSubmit(onSubmit)}>
        <FormControl isRequired>
          <FormLabel htmlFor="username">Username</FormLabel>
          <Input
            id="username"
            focusBorderColor="yellow.200"
            type="text"
            {...register("username", {
              required: "This is required",
            })}
          />
        </FormControl>
        <FormControl isRequired>
          <FormLabel htmlFor="password">Password</FormLabel>
          <Input
            id="password"
            focusBorderColor="yellow.200"
            type="password"
            {...register("password", {
              required: "This is required",
            })}
          />
        </FormControl>
        <FormControl isRequired>
          <FormLabel htmlFor="email">Email</FormLabel>
          <Input
            id="email"
            focusBorderColor="yellow.200"
            type="email"
            {...register("email", {
              required: "This is required",
            })}
          />
          {!isDirty && (
            <FormHelperText>
              Enter the message you would like to send me.
            </FormHelperText>
          )}
          {errors && (
            <>
              <FormErrorMessage>{errors?.username?.message}</FormErrorMessage>
              <FormErrorMessage>{errors?.password?.message}</FormErrorMessage>
              <FormErrorMessage>{errors?.email?.message}</FormErrorMessage>
            </>
          )}
        </FormControl>
        {/* <div className="flex justify-center"> */}
        <Button
          as={motion.div}
          initial="initial"
          animate="animate"
          whileHover="hover"
          whileTap="tap"
          variants={rClickables}
          mt={4}
          isLoading={isSubmitting}
          type="submit"
          className="cursor-pointer flex-auto"
          onClick={() => {
            console.log("clicked");
          }}
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
        {/* </div> */}
      </form>
    </Container>
  );
};

export default ContactForm;