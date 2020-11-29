import React, { useMemo, useState } from "react";

import { UserContextT, UserT } from "types/userContext";

const UserContext = React.createContext<UserContextT | null>(null);

const UserProvider: React.FC = ({ children }) => {
  const [state, setState] = useState<UserT>();

  const value = useMemo(() => ({ userState: state, setUserState: setState }), [
    state,
  ]);

  return <UserContext.Provider value={value}>{children}</UserContext.Provider>;
};

export { UserProvider, UserContext };

export type { UserT, UserContextT } from "../../types/userContext";
