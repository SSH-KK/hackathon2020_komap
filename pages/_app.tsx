import React from 'react'

import "styles/globals.css";
import { CounterProvider } from "context/counterContext";

function MyApp({ Component, pageProps }) {
  return (
    // Здесь компонент Component оборачиваем провайдеры глобального контекста. Если контекст используется не во всём приложении, а в каком-то определённом компоненте и его дочерних элементах, стоит занести провайдер туда
    <CounterProvider>
      <Component {...pageProps} />
    </CounterProvider>
  );
}

export default MyApp;
