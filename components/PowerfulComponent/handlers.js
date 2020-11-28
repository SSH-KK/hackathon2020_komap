// Лучше писать документацию на функции, за это будет респект от менторов
/**
 * Increase counter
 * @param {SetStateAction} setCounter
 */
const handleCounterClick = (setCounter) => {
  return () => setCounter((prev) => prev + 1); // Если используем контекст, тогда замыкаем всё, что нужно внутри обработчика
};

// Экспорт лучше делать отдельно, чтобы всегда знать, что мы экспортируем из файла, а что используем внутри (как с public/private методами)
export { handleCounterClick };
