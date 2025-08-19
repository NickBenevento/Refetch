import { getUserName } from "../services/userService";

const Header = ({ userID }: { userID: string | null }) => {
  // const Header = ({userID: string | null}) => {
  const userName = getUserName();

  return (
    <div>
      {userID ? (
        <div>
          Logged in as User: {userName}, id={userID}
        </div>
      ) : (
        <div>Not logged in </div>
      )}
    </div>
  );
};

export default Header;
