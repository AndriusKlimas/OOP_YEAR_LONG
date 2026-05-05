from user_data_access import *
from user_records import User

class UserService:
    def __init__(self, user_data):
        self.__user_data = user_data

        self.__usable_user_data = {}


    def load_serv_user(self):
        if not self.__user_data:
            raise AttributeError("No user_data class present- cannot load data")

        self.__usable_user_data = self.__user_data.load()

        # Print all loaded usernames, for testing
        print("\n✅ Users loaded:")
        for username in self.__usable_user_data.keys():
            print(f"  - {username}")
        print(f"Total users: {len(self.__usable_user_data)}\n")

    def user_login_serv(self, username, password) -> tuple[bool, str]:
        """ validatying the info provided by the user

        Returns:
            tuple[bool, str]: A tuple containing:
                - bool: False if login successful, True if login failed
                - str: Username if successful, error message if failed
        """


        try:
            if username not in self.__usable_user_data:
                logger.info("user_login: username not in dictionary")
                return True, "Username not found"

            try:
                user = User.validate_login(self.__usable_user_data, username, password)
            except Exception as e:
                logger.error("user_login: unexpected error when validating username/password %s", e)
                return True, "Error logging in"

            if user is not None:
                self.__usable_user_data[username] = user
                logger.info("user_login: successfully logged in")
                return False, username
            else:
                logger.info("user_login: failed to log in")
                return True, "invalid username or password"

        except KeyError:
            logger.error("KeyError in user_login: Users dictionary not found: %s", e)
            return True, "Error: Users dictionary not accessible"
        except Exception as e:
            logger.error("Unexpected error during user_login: %s", e)
            return True, "An unexpected error occurred during login"


    def create_login_srv(self, username, password) -> tuple[bool, str]:
        try:
            # Checking is the username already exists
            if username in self.__usable_user_data:
                logger.info("user_login: username already exists")
                return True, f"username {username} already exists"
            else:
                valid_password = User.validate_password(password)
                logger.info("user_login: validating password")

                if valid_password:
                    # creating the class object
                    new_user = User(username, password)
                    logger.info("user_login: created new user")

                    # saving user to local dictionary
                    self.__usable_user_data[username] = new_user

                    # saving to json file
                    self.__user_data.store(self.__usable_user_data)

                    return False, username

                else:
                    logger.info("user_login: password not pass validation")
                    return True, "password does not meet minimum requirements"

        except KeyError as e:
            logger.error("KeyError in create_login: Users dictionary not found %s", e)
            return True, "Error: Users dictionary not accessible"

        except ValueError as e:
            logger.error("ValueError in create_login: Invalid input provided %s", e)
            return True, "Error: Invalid input"
        except Exception as e:
            logger.error("Unexpected error during create_login: %s", e)
            return True, "An unexpected error occurred during account creation"


