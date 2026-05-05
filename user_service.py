from user_data_access import *

class UserService:
    def __init__(self, user_data):
        self.__user_data = user_data

        self.__usable_user_data = {}


    def load_serv(self):
        if not self.__user_data:
            raise AttributeError("No user_data class present- cannot load data")

        self.__usable_user_data = self.__user_data.load()

        # Print all loaded usernames, for testing
        print("\n✅ Users loaded:")
        for username in self.__usable_user_data.keys():
            print(f"  - {username}")
        print(f"Total users: {len(self.__usable_user_data)}\n")





    # def user_login_service(self, username, password):
    #     #here is also just checking
    #     try:
    #         username = input().strip()
    #         if username not in self.__user_data:
    #             logger.info("user_login: username not in dictionary")
    #             print("Username not found. Please try again.")
    #             return True, "Username not found"
    #         #need to remove this shit and make it work better
    #         print("Enter password:")
    #         password = input().strip()
    #
    #         #here i am just cheking and validating that it will work as a login
    #         try:
    #             user = User.validate_login(self.__user_data,username, password)
    #
    #         except Exception as e:
    #             logger.error("user_login: unexpected error when validating username/password %s", e)
    #             print(f"Error logging in: {e}")
    #
    #             return True, "Error logging in"
    #         #I am appending it here
    #         if user is not None:
    #             self.__user_data[username] = user
    #             logger.info("user_login: successfully logged in")
    #             print(f"Logging in as {username}")
    #             return False, username
    #         else:
    #             logger.info("user_login: failed to log in")
    #             return True, "invalid username or password"
    #
    #     except KeyError:
    #         logger.error("KeyError in user_login: Users dictionary not found: %s", e)
    #         print("User dictionary not found")
    #         return True, "Error: Users dictionary not accessible"
    #     except Exception as e:
    #         logger.error("Unexpected error during user_login: %s", e)
    #         print(f"An error occurred during login: {e}")
    #         return True, "An unexpected error occurred during login"


