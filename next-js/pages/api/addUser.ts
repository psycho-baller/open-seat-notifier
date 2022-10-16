// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import { Prisma } from '@prisma/client';
import type { NextApiRequest, NextApiResponse } from 'next/types'
import prisma from "../../lib/prisma";

interface where{
  email: string;
}

export default async (req: NextApiRequest, res: NextApiResponse) => {
  if (req.method !== "POST") {
    return res
      .status(405)
      .json({ message: `${req.method} requests are not allowed` });
  }
  const { email, username, password } = JSON.parse(req.body);

  const user = {
    email: email as string,
    username: username as string,
    password: password as string,
    // id: parseInt(Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15),10)
    // notified_studies: [],
  };
  try {
    // checks if user already exists, and if found, edit the user's data
    const result = await prisma.main.upsert({
      where: {
        email: user.email as string,
      } as Prisma.mainWhereUniqueInput,
      update: {
        username: user.username,
        password: user.password,
      },
      create: {
        email: user.email,
        username: user.username,
        password: user.password,
      },
    });
    
    // const addUser = await prisma.main.create({ data: user });
    console.log(result);
    res.status(201).json({
      message: "User created successfully",
      data: result,
    });
  } catch (error: any) {
    console.log(error);
    res.status(500).send(error);
    res.json({ error: error.message });
  }
};
