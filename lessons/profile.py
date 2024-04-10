"""Practice Writing a Class."""

#Definition
class Profile:

    username: str
    private: bool 

    def __init__(self, username_input: str):
        """Create a new Profile object."""
        self.username = username_input
        self.private = True

    def tweet(self, msg: str):
        """If Profile is Public, print message."""
        if self.private == False:
            print(msg)

#Instantiating 
user1: Profile = Profile("110_rulez") # calls __init__()
user1.private = False
user1.tweet("OOP is cool!")