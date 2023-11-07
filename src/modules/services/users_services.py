from passlib.context import CryptContext

class UserServices:
    
    def __init__(self):
        self._password_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
        
    
    def hash_password(self, password):
        return self._password_context.hash(password)
    