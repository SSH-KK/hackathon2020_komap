type RouteT = {
  id: number;
  name: string;
  length: number;
  averageTime?: number;
  userTime?: number;
  startCoordinates?: CoordinatesT;
  coordinates?: CoordinatesT[];
};

type CoordinatesT = {
  latitude: number;
  longitude: number;
};

export type { RouteT, CoordinatesT };
