import React from "react";
import { IRouteView } from "types/user";
import RouteCard from "./RouteCard";

const RouteView: React.FC<IRouteView> = ({ header, routes }) => {
  return (
    <>
      <h1>{header}</h1>
      {routes.map((route) => (
        <RouteCard key={route.id} route={route} />
      ))}
    </>
  );
};

export default RouteView;
