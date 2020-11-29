const formatTimeLength = (minutes: number) =>
  (Math.floor(minutes / 60) > 0 ? `${Math.floor(minutes / 60)} ч. ` : "") +
  (minutes % 60 > 0 ? `${minutes % 60} мин.` : "");

const request = async (uri: string, method: "POST" | "GET", body = null) => {
  const url = "http://localhost:4000/api/" + uri;

  const headers = {
    "Content-Type": "application/json",
    method,
    body: method == "POST" ? body : undefined,
  };

  const options = {
    headers,
    body: method == "GET" ? body : undefined,
  };

  try {
    if (process.env.NODE_ENV == "development") {
      return JSON.parse(`{ "token": "fhjighdfjgjdfigbvhbsdfuyt47" }`);
    }
    const res = await fetch(url, options);
    return await res.json();
  } catch (err) {
    console.log(err.message);
    throw err;
  }
};

export { formatTimeLength, request };
