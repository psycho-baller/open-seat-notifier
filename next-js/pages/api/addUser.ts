// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'
import prisma from "../../lib/prisma";
import { Prisma } from "@prisma/client";

export default async (req: NextApiRequest, res: NextApiResponse) => {
  const { email, username, password } = JSON.parse(req.body);

  // @ts-ignore
  const user: Prisma.UserCreateInput = {
    email: email,
    username: username,
    password: password,
  };
  try {
    // @ts-ignore
    const addUser = await prisma.user.create({ data: user });
    console.log(addUser);
    res.status(201).json({
      message: "User created successfully",
      data: addUser,
    });
  } catch (error: any) {
    console.log(error);
    res.status(500).send(error);
    res.json({ error: error.message });
  }
};
