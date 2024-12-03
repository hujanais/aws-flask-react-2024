class AuthService:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(AuthService, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not hasattr(self, "isAuthenticated"):
            self.isAuthenticated = False

    def login(self):
        self.isAuthenticated = True

    def logout(self):
        self.isAuthenticated = False
