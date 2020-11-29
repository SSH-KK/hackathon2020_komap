import React, { Dispatch, FormEvent, SetStateAction, useContext } from "react";
import { NextRouter, useRouter } from "next/router";

import ErrorMessage from "components/ErrorMessage";
import { UserContext, UserT } from "context/user";
import useErrorHandler from "hooks/ErrorHandler";
import { request } from "utils/index";

const dispatch = (err: Error) => "Error happened";

const setToken = async (
  token: string,
  setUserState: Dispatch<SetStateAction<UserT>>
) => {
  localStorage.setItem("token", token);
  try {
    const user = await request("user", "GET");

    setUserState(user);
  } catch (err) {
    console.log(err.message);
    throw err;
  }
};

const handleSubmit = (
  resetError: () => void,
  setUserState: Dispatch<SetStateAction<UserT>>,
  gotError: (err: Error) => void,
  router: NextRouter
) => async (e: FormEvent<HTMLFormElement>) => {
  e.preventDefault();

  try {
    const formData = new FormData(e.currentTarget);
    const jsonData = Object.fromEntries(formData);

    resetError();

    const res = await request("login", "POST", jsonData);

    setToken(res.token, setUserState);

    router.push("/user");
  } catch (err) {
    gotError(err.message);
  }
};

const Login: React.FC = () => {
  const router = useRouter();
  const { error, gotError, resetError } = useErrorHandler(dispatch);
  const { userState, setUserState } = useContext(UserContext);

  return (
    <form onSubmit={handleSubmit(resetError, setUserState, gotError, router)}>
      <input type="username" name="username" id="username" />
      <input type="password" name="password" id="password" autoComplete="on" />
      <input type="submit" />
      {error.has ? <ErrorMessage message={error.message} /> : ""}
    </form>
  );
};

export default Login;
