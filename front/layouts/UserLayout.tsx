import React, { useContext } from "react";

import Header from "components/User/header";
import { UserContext } from "context/user";

const UserLayout: React.FC = ({ children }) => {
  const { userState } = useContext(UserContext);
  return (
    <>
      <Header points={userState.points} />
      <main>{children}</main>
    </>
  );
};

export default UserLayout;
