import { useState } from "react";
import {
  getUserIDFromSession,
  getUserName,
  setUserName,
} from "../../services/userService";

interface userProps {
  userID: string | null;
  setUserID: (id: string | null) => void;
}

const UserInfo: React.FC<userProps> = (props) => {
  const { userID, setUserID } = props;
  // const userInfo({ userID, setUserID }: userProps) => {
  const [input, setInput] = useState("");

  // Correct type for input change event
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>): void => {
    setInput(event.target.value);
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>): void => {
    event.preventDefault();
    setUserName(input);
    const newID = getUserIDFromSession();
    if (newID) {
      setUserID(newID);
    }
  };

  return (
    <div className="mb-4 text-white">
      {userID ? (
        <p>
          Logged in as User {getUserName()} with ID: {userID}
        </p>
      ) : (
        <form onSubmit={handleSubmit}>
          <label>
            Input your name:
            <input
              type="text"
              value={input}
              onChange={handleChange} // no need for arrow function here
              className="p-2 rounded text-black"
            />
          </label>
          <button
            type="submit"
            className="ml-2 bg-blue-500 text-white px-4 py-2 rounded"
          >
            Submit
          </button>
        </form>
      )}
    </div>
  );
};

export default UserInfo;
