import React from "react";
import { IRouteView } from "types/user";
import RouteCard from "./RouteCard";

import styles from "styles/RouteView.module.css";

const RouteView: React.FC<IRouteView> = ({ header, routes }) => {
  return (
    <>
      <h2 className={styles.header}>{header}</h2>
      {routes.map((route) => (
        <RouteCard key={route.id} route={route} />
      ))}
    </>
  );
};

export default RouteView;
