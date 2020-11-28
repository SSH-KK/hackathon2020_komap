import React from "react";

import { IRouteCard } from "types/user";
import { formatTimeLength } from "utils";

const RouteCard: React.FC<IRouteCard> = ({ route }) => {
  return (
    <div>
      <h2>{route.name}</h2>
      <p>
        Данный квесты вы сможете пройти за {formatTimeLength(route.averageTime)}
      </p>
      <p>Длинна маршрута: {route.length} м</p>
      <p>Примерное время прохождения: {route.averageTime}</p>
      <p>Точка старта:</p>
    </div>
  );
};

export default RouteCard;
