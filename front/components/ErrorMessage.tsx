import React from "react";

import styles from "styles/errorMessage.module.css";

interface IErrorMessageProps {
  message: string;
}

const ErrorMessage: React.FC<IErrorMessageProps> = ({ message }) => (
  <div>
    <p className={styles.text}>{message}</p>
  </div>
);

export default ErrorMessage;
