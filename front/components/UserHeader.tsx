import { UserContext } from "context/user";
import Link from "next/link";
import React, { useContext } from "react";

const UserHeader: React.FC = () => {
  const user = useContext(UserContext);

  return (
    <>
      <div>Очки: {user?.userState?.points || 0}</div>
      <nav>
        <ul>
          <li>
            <Link href="/profile">
              <a>Профиль</a>
            </Link>
          </li>
          <li>
            <Link href="/achivements">
              <a>Ачивки</a>
            </Link>
          </li>
        </ul>
      </nav>
    </>
  );
};

export default UserHeader;
