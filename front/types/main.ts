type FCL = React.FC & { Layout: React.ReactNode };

type RouteT = {
  id: number;
  name: string;
  description: string;
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

export type { FCL, RouteT, CoordinatesT };
