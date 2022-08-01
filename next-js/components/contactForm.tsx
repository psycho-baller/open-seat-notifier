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
import prisma from "../lib/prisma";
import {Prisma}  from '@prisma/client';


const ContactForm = () => {
  const toast = useToast();
  const {
    handleSubmit,
    register,
    formState: { errors, isSubmitting, isDirty },
  } = useForm({ defaultValues: { username: "", password: "", email: "" } });
  async function onSubmit(data: any) {
    // @ts-ignore
    const user: Prisma.UserCreateInput = {
      email: data.email,
      username: data.username,
      password: data.password,
    };
    try {
      // @ts-ignore
      const addUser = await prisma.user.create({data: user});
      console.log(addUser);
      toast({
        title: "User added successfully",
        description: "You will recieving emails whenever new studies are up",
        status: "success",
        duration: 9000,
        isClosable: true,
      });
    }
    catch (error) {
      console.log(error);
      toast({
        title: "Error adding user",
        description: "Please try again",
        status: "error",
        duration: 3000,
        isClosable: true,
      });
    }
  }
  return (
    <Container p={4}>
      <Heading p={2}>Plz lemme hack u</Heading>

      <form action="" onSubmit={handleSubmit(onSubmit)}>
        <FormControl isRequired>
          <FormLabel htmlFor="name">Username</FormLabel>
          <Input
            focusBorderColor="yellow.200"
            {...register("username", {
              required: "This is required",
            })}
            id="name"
            type="text"
          />
        </FormControl>
        <FormControl isRequired>
          <FormLabel id="email">Password</FormLabel>
          <Input
            focusBorderColor="yellow.200"
            {...register("password", {
              required: "This is required",
            })}
            type="email"
          />
        </FormControl>
        <FormControl isRequired>
          <FormLabel id="email">Email</FormLabel>
          <Input
            focusBorderColor="yellow.200"
            {...register("email", {
              required: "This is required",
            })}
            type="email"
          />
          {!isDirty && (
            <FormHelperText>
              Enter the message you would like to send me.
            </FormHelperText>
          )}
          {errors.email && (
            <FormErrorMessage>{errors.email.message}</FormErrorMessage>
          )}
        </FormControl>
        <div className="flex justify-center">
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