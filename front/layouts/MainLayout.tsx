import React from "react";

import styles from "styles/layout.module.css";
import { UserProvider } from "context/user";

const Layout: React.FC = ({ children }) => {
  return (
    <UserProvider>
      <div className={styles.content}>{children}</div>
    </UserProvider>
  );
};

export default Layout;
