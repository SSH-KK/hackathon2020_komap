const formatTimeLength = (minutes: number) =>
  (Math.floor(minutes / 60) > 0 ? `${Math.floor(minutes / 60)} ч. ` : "") +
  (minutes % 60 > 0 ? `${minutes % 60} мин.` : "");

export { formatTimeLength };
