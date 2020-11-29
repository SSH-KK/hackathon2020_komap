import { request } from "utils/index";
import React, { useEffect } from "react";
import { useRouter } from "next/router";
import { redirect } from "next/dist/next-server/server/api-utils";

const Activate: React.FC = () => {
  const router = useRouter();

  useEffect(() => {
    (async () => {
      const res = await request(
        `activate/${router.query.uidb}/${router.query.token}`,
        "POST"
      );

      router.push("/");
    })();
  });
  return null;
};

export default Activate;
