import React from "react";
import { motion } from "framer-motion";

import "styles/globals.css";
import Layout from "components/Layout";
import { AppProps } from "next/dist/next-server/lib/router/router";
import { UserProvider } from "context/user";
import { HomeRefProvider } from "context/ref";
import { LoadingProvider } from "context/loading";

function MyApp({ Component, pageProps, router }: AppProps) {
  return (
    <LoadingProvider>
      <UserProvider>
        <HomeRefProvider>
          <Layout pathname={router.pathname}>
            <motion.div
              initial="pageInitial"
              animate="pageAnimate"
              variants={{
                pageInitial: {
                  opacity: 0,
                },
                pageAnimate: {
                  opacity: 1,
                },
              }}
              key={router.route}
            >
              <Component {...pageProps} />
            </motion.div>
          </Layout>
        </HomeRefProvider>
      </UserProvider>
    </LoadingProvider>
  );
}

export default MyApp;
