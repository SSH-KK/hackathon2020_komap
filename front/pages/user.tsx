import UserLayout from "layouts/UserLayout";
import { UserContext } from "context/user";
import React, { useContext } from "react";
import RouteView from "components/User/RouteView";
import { RouteT } from "types/main";

const routes: RouteT[] = [
  {
    id: 0,
    name: "Пешком",
    length: 100,
    averageTime: 100,
    startCoordinates: {
      latitude: 60.977313,
      longitude: 69.039326,
    },
  },
];

const User = () => {
  const { userState, setUserState } = useContext(UserContext);
  return (
    <>
      <RouteView header={"Новые маршруты"} routes={routes} />
    </>
  );
};

User.Layout = UserLayout;

export default User;
