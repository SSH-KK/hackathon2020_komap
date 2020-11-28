import { useState } from "react";

// Если функционал можно где-то переиспользовать или если код логики компонента занимает больше 150 строк, стоит разбить его на кастомные хуки и вынести сюда
/**
 * Simple counter hook
 * @param {number} initialState
 */
const useCounter = (initialState = 0) => {
  if (typeof initialState !== "number")
    throw new Error("Initial counter state must be a number");

  const [counter, setCounter] = useState(initialState);

  const increaseCounter = () => {
    setCounter((prev) => prev + 1);
  };

  return { counter, increaseCounter };
};

export { useCounter }