import React from "react";
import { useCounter } from "hooks/counter";

const Counter = () => {
  const { counter, increaseCounter } = useCounter();

  return (
    <div>
      <h1>{counter}</h1>
      <button onClick={increaseCounter}>+</button>
    </div>
  );
};

export default Counter