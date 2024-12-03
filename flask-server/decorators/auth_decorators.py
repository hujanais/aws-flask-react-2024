from functools import wraps
from services.auth_service import AuthService


# Authorization decorator
def requires_authorization(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if AuthService().isAuthenticated == False:
            return {"error": "Unauthorized"}, 401
        return f(*args, **kwargs)

    return decorated_function
