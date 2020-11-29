import React, { FormEvent, useState } from "react";

import ErrorMessage from "components/ErrorMessage";
import useErrorHandler from "hooks/ErrorHandler";
import { request } from "utils/index";

const dispatch = (err: Error) => "Error happened";

const Register: React.FC = () => {
  const [successfulAttempt, setSuccessfulAttempt] = useState<boolean>(false);
  const { error, gotError, resetError } = useErrorHandler(dispatch);

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const formData = new FormData(e.currentTarget);
      const jsonData = Object.fromEntries(formData);

      resetError();

      const res = await request("register", "POST", jsonData);

      if (!res.ok) throw new Error("Couldn't register");

      setSuccessfulAttempt(true);
    } catch (err) {
      gotError(err.message);
    }
  };

  return successfulAttempt ? (
    <p>
      Для продолжения регистрации перейдите по ссылке, отправленной вам на
      введённую почту
    </p>
  ) : (
    <form onSubmit={handleSubmit}>
      <input type="text" name="username" id="username" />
      <input type="email" name="email" id="email" />
      <input type="password" name="password" id="password" autoComplete="on" />
      <input type="submit" />
      {error.has ? <ErrorMessage message={error.message} /> : ""}
    </form>
  );
};

export default Register;
