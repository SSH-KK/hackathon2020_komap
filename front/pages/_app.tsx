import React from "react";

import "styles/globals.css";
import Layout from "layouts/MainLayout";
import EmptyLayout from "layouts/EmptyLayout";

function MyApp({ Component, pageProps }) {
  const ComponentLayout = Component.Layout || EmptyLayout;
  return (
    <Layout>
      <ComponentLayout>
        <Component {...pageProps} />
      </ComponentLayout>
    </Layout>
  );
}

export default MyApp;
