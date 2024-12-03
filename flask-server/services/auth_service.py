# Singleton class to manage authentication state
class AuthService:
    def __new__(cls):
        print("AuthService.__new__")
        if not hasattr(cls, "instance"):
            print("AuthService.__new__ creating instance")
            cls.instance = super(AuthService, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        print("AuthService.__init__")
        if not hasattr(self, "isAuthenticated"):
            print("AuthService.__init__ initializing")
            self.isAuthenticated = False

    def login(self):
        self.isAuthenticated = True

    def logout(self):
        self.isAuthenticated = False
