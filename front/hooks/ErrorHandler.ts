import { useState } from "react";

type ErrorT = {
  message?: string;
  has: boolean;
};

const useErrorHandler = <T extends Function>(
  dispatcher: T
): {
  error: ErrorT;
  gotError: (err: Error) => void;
  resetError: () => void;
} => {
  const [error, setError] = useState<ErrorT>({ has: false });

  const gotError = (err: Error) =>
    setError({ has: true, message: dispatcher(err) });

  const resetError = () => setError({ has: false });

  return { error, gotError, resetError };
};

export default useErrorHandler;
