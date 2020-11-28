import React from "react";
import Link from "next/link";

import { IHeaderProps } from "types/user";

const Header: React.FC<IHeaderProps> = ({ points }) => {
  return (
    <header>
      <div>Очки: {points}</div>
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
    </header>
  );
};

export default Header;
