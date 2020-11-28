import { RouteT } from "./main";

interface IHeaderProps {
  points: number;
}

interface IRouteView {
  header: string;
  routes: RouteT[];
}

interface IRouteCard {
  route: RouteT;
}

export type { IHeaderProps, IRouteView, IRouteCard };
