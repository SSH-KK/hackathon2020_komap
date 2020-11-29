import React, { useContext, useEffect, useState } from "react";

import styles from "styles/home.module.css";
import { HomeRefContext } from "context/ref";
import Register from "components/Register";
import Login from "components/Login";
import { UserContext } from "context/user";
import { useRouter } from "next/router";
import { LoadingContext } from "context/loading";

const advantagesList = [
  {
    icon: "home/map.svg",
    alt: "Map",
    text:
      "Поиск маршрутов для прогулки по знаковым местам незнакомомого города",
  },
  {
    icon: "home/coin.svg",
    alt: "Coin",
    text: "Бесплатный сервис по всей Югре",
  },
  {
    icon: "home/dialog.svg",
    alt: "Dialog",
    text: "Новые знакомства и общение",
  },
];

const Home: React.FC = () => {
  const { setLoading } = useContext(LoadingContext);
  const { userState } = useContext(UserContext);
  const router = useRouter();

  useEffect(() => {
    if (userState) {
      router.push("/user");
      return null;
    } 
    else setLoading(false);
  }, []);

  const scrollRef = useContext(HomeRefContext);

  const [newUser, setNewUser] = useState<boolean>(true);

  return (
    <>
      <div className={styles.picCard}>
        <p className={styles.picMainText}>
          Туристический
          <br />
          квест
        </p>
        <p className={styles.picSubText}>
          Увлекательное путешествие в форме квеста без скучного поиска новых,
          интересных мест
        </p>
      </div>
      <ul className={styles.advantages}>
        {advantagesList.map((element, key) => (
          <li className={styles.advantage} key={key}>
            <img
              className={styles.advantageIcon}
              src={element.icon}
              alt={element.alt}
            />
            <p className={styles.advantageText}>{element.text}</p>
          </li>
        ))}
      </ul>
      <div ref={scrollRef} className={styles.authContainer}>
        <h2 className={styles.authHeader}>
          Поле для <a onClick={() => setNewUser(true)}>регистрации</a>/
          <a onClick={() => setNewUser(false)}>входа</a>
        </h2>
        {newUser ? <Register /> : <Login />}
      </div>
    </>
  );
};

export default Home;
