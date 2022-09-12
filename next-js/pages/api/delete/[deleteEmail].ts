import type { NextApiRequest, NextApiResponse } from "next/types";
import prisma from "../../../lib/prisma";

export default async (req: NextApiRequest, res: NextApiResponse) => {
  const { deleteEmail } = req.query;

  if (deleteEmail) {
    const result = await prisma.main.deleteMany({
      where: {
        email: {
          contains: deleteEmail as string,
        },
      },
    });
    if (result.count > 0) {
      res.status(200).json({ message: `User deleted successfully, ${deleteEmail} will no longer receive emails` });
    } else {
      res.status(404).json({ message: `${deleteEmail} not found` });
    }
  } else {
    res.status(400).json({ error: "Missing email" });
  }
};
