import React, { Dispatch, SetStateAction, useMemo, useState } from "react";

const LoadingContext = React.createContext<LoadingContextT>(null);

type LoadingContextT = {
  loading: boolean;
  setLoading: Dispatch<SetStateAction<boolean>>;
};

const LoadingProvider: React.FC = ({ children }) => {
  const [loading, setLoading] = useState<boolean>(true);

  const value = useMemo<LoadingContextT>(() => ({ loading, setLoading }), [
    loading,
  ]);

  return (
    <LoadingContext.Provider value={value}>{children}</LoadingContext.Provider>
  );
};

export { LoadingContext, LoadingProvider };
