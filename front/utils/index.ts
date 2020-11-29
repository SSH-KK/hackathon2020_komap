const formatTimeLength = (minutes: number) =>
  (Math.floor(minutes / 60) > 0 ? `${Math.floor(minutes / 60)} ч. ` : "") +
  (minutes % 60 > 0 ? `${minutes % 60} мин.` : "");

const request = async (uri: string, method: "POST" | "GET", body?) => {
  const token = localStorage.getItem("token");

  const url = "http://80.240.25.179/api/" + uri;

  const headers = {
    "Content-Type": "application/json",
    Authorization: token != "" ? `Token ${token}` : undefined,
  };

  const options = {
    headers,
    method,
    body: JSON.stringify(body),
  };

  console.log(uri);

  try {
    // if (process.env.NODE_ENV == "development") {
    //   return JSON.parse(`{ "token": "fhjighdfjgjdfigbvhbsdfuyt47" }`);
    // }
    const res = await fetch(url, options);
    return await res.json();
  } catch (err) {
    console.log(err.message);
    throw err;
  }
};

export { formatTimeLength, request };
