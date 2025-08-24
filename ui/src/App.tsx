import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import Header from "./components/header";
import "./App.css";
import ProductPage from "./components/product/ProductPage";
import UserInfo from "./components/user/User";
import { getUserIDFromSession } from "./services/userService";

function App() {
  const [count, setCount] = useState(0);
  const [userID, setUserID] = useState<string | null>(null);

  // Initial useEffect to fetch userID from sessionStorage
  useEffect(() => {
    const id = getUserIDFromSession();
    setUserID(id);
  }, []);

  return (
    <div className="w-screen min-h-screen bg-cyan-700 items-center justify-center flex flex-col">
      <Header userID={userID} />
      {userID ? (
        <div>
          <ProductPage />
        </div>
      ) : (
        <UserInfo userID={userID} setUserID={setUserID} />
      )}
    </div>
  );
}

export default App;
