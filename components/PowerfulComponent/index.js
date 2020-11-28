import React, { useCallback, useContext } from "react";

import { CounterContext } from "context/counterContext";
import { handleCounterClick } from "./handlers"; // Обработчики событий лучше держать в отдельном файле или использовать кастомные хуки

/**
 * Complex component with counter with context in it
 */
const PowerfulComponent = () => {
  const context = useContext(CounterContext);

  console.log(context);

  const handleClick = useCallback(handleCounterClick(context.setCounter), [
    context.setCounter,
  ]);

  return (
    <div>
      <h1>{context?.counter}</h1>
      <button onClick={handleClick}>Increase</button>
    </div>
  );
};

export default PowerfulComponent;
