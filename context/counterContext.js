import React, { useEffect, useMemo, useState } from "react";

const CounterContext = React.createContext(null);

const initialContext = 0;

const CounterProvider = ({ children }) => {
  const [counter, setCounter] = useState(null);

  useEffect(() => {
    // Тут что-то делать для инициализации контекста
    setCounter(initialContext); // Например
  }, []);

  const value = useMemo(() => ({ counter, setCounter }), [counter]); // На самом деле, в случе нашего проекта это мало повлияет на производительность, но в каком-то туториале советовали так делать, поэтому почему бы и нет

  return (
    <CounterContext.Provider value={value}>{children}</CounterContext.Provider>
  );
};

export { CounterContext, CounterProvider };
