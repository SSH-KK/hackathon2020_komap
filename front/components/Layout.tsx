import React, { useContext, useEffect, useState } from "react";

import styles from "styles/layout.module.css";
import { LoadingContext } from "context/loading";
import HomeHeader from "./HomeHeader";
import UserHeader from "./UserHeader";

const Layout: React.FC<{ pathname: string }> = ({ children, pathname }) => {
  const { loading, setLoading } = useContext(LoadingContext);

  useEffect(() => setLoading(false), []);

  if (loading) return <h1>Loading...</h1>;

  return (
    <div className={styles.content}>
      <nav className={styles.header}>
        <div className={styles.logo}>
          <img src="logo.svg" alt="" />
          <p className={styles.textLogo}>Ko.Map</p>
        </div>
        <div />
        <div>
          {pathname == "/" ? <HomeHeader /> : ""}
          {pathname == "/user" ? <UserHeader /> : ""}
        </div>
      </nav>
      <div>{children}</div>
    </div>
  );
};

export default Layout;
