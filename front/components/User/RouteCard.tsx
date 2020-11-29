import React from "react";

import { IRouteCard } from "types/user";

const RouteCard: React.FC<IRouteCard> = ({ route }) => {
  return (
    <div>
      <h3>{route.name}</h3>
      <p>{route.description}</p>
      <p>Длинна маршрута: {route.length} м</p>
      <p>Примерное время прохождения: {route.averageTime}</p>
      <p>Точка старта:</p>
    </div>
  );
};

export default RouteCard;
