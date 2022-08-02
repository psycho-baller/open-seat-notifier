// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'
import prisma from "../../lib/prisma";
import { Prisma } from "@prisma/client";

export default async (req: NextApiRequest, res: NextApiResponse) => {
  if (req.method !== "POST") {
    return res
      .status(405)
      .json({ message: `${req.method} requests are not allowed` });
  }
  const { email, username, password } = JSON.parse(req.body);

  // @ts-ignore
  const user = {
    email: email,
    username: username,
    password: password,
    id: parseInt(Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15),10)
    // notified_studies: [],
  };
  try {
    const addUser = await prisma.main.create({ data: user });
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
