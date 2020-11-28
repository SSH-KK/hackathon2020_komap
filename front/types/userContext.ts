import { Dispatch, SetStateAction } from "react";

export type UserT = {
  username: string;
  email: string;
  id: number;
  points: number;
};

export type UserContextT = {
  userState: UserT;
  setUserState: Dispatch<SetStateAction<UserT>>;
};
