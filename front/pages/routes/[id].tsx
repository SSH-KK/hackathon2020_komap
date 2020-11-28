import React from "react";
import { YMaps, Map, Placemark } from "react-yandex-maps";
import { RouteT } from "types/main";

const route: RouteT = {
  id: 0,
  length: 10,
  name: "Тест",
  averageTime: 10,
  startCoordinates: {
    latitude: 10,
    longitude: 10,
  },
};

const Route: React.FC = () => {
  return (
    <YMaps>
      <Map
        defaultState={{
          center: [
            route.startCoordinates.latitude,
            route.startCoordinates.longitude,
          ],
          zoom: 14,
        }}
      >
        <Placemark
          geometry={[
            route.startCoordinates.latitude,
            route.startCoordinates.longitude,
          ]}
        />
      </Map>
    </YMaps>
  );
};

export default Route;
