import React, { MutableRefObject, useRef } from "react";

const HomeRefContext = React.createContext<MutableRefObject<HTMLDivElement>>(
  null
);

const HomeRefProvider: React.FC = ({ children }) => {
  const value = useRef<HTMLDivElement>(null);

  return (
    <HomeRefContext.Provider value={value}>{children}</HomeRefContext.Provider>
  );
};

export { HomeRefContext, HomeRefProvider };
