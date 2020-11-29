import { UserContext } from "context/user";
import React, { useContext } from "react";
import RouteView from "components/User/RouteView";
import { RouteT } from "types/main";
import { useRouter } from "next/router";

const routes: RouteT[] = [
  {
    id: 0,
    name: "Пешком",
    length: 100,
    averageTime: 100,
    description:
      "Ipsum do irure ut excepteur reprehenderit nulla proident cupidatat ullamco officia pariatur enim consequat.",
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

export default User;
