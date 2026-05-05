from user_data_access import *

class UserService:
    def __init__(self, user_data):
        self.__user_data = dict.copy(user_data) if user_data else {}


    def user_login_service(self, username, password):
        #here is also just checking
        try:
            username = input().strip()
            if username not in self.__user_data:
                logger.info("user_login: username not in dictionary")
                print("Username not found. Please try again.")
                return True, "Username not found"
            #need to remove this shit and make it work better
            print("Enter password:")
            password = input().strip()

            #here i am just cheking and validating that it will work as a login
            try:
                user = User.validate_login(self.__user_data,username, password)

            except Exception as e:
                logger.error("user_login: unexpected error when validating username/password %s", e)
                print(f"Error logging in: {e}")

                return True, "Error logging in"
            #I am appending it here
            if user is not None:
                self.__user_data[username] = user
                logger.info("user_login: successfully logged in")
                print(f"Logging in as {username}")
                return False, username
            else:
                logger.info("user_login: failed to log in")
                return True, "invalid username or password"

        except KeyError:
            logger.error("KeyError in user_login: Users dictionary not found: %s", e)
            print("User dictionary not found")
            return True, "Error: Users dictionary not accessible"
        except Exception as e:
            logger.error("Unexpected error during user_login: %s", e)
            print(f"An error occurred during login: {e}")
            return True, "An unexpected error occurred during login"


