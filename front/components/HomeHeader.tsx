import { HomeRefContext } from "context/ref";
import React, { useContext } from "react";

import styles from "styles/layout.module.css";

const HomeHeader: React.FC = () => {
  const ref = useContext(HomeRefContext);

  const scrollToRef = () => ref?.current?.scrollIntoView();

  return (
    <a onClick={scrollToRef} className={styles.link}>
      Регистрация
    </a>
  );
};

export default HomeHeader;
