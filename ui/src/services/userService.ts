export const getUserIDFromSession = (): string | null => {
  const userID = sessionStorage.getItem("userID");
  return userID;
};

export const getUserName = (): string | null => {
  return sessionStorage.getItem("userName");
};

export const setUserName = (name: string): void => {
  const userID = `user-${Math.random().toString(36).substr(2, 9)}`;
  sessionStorage.setItem("userID", userID);
  sessionStorage.setItem("userName", name);
};
