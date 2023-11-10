from passlib.context import CryptContext

class PasswordServices:
    def __init__(self):
        self._password_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def hash_password(self, plain_password):
        return self._password_context.hash(plain_password)
    
    def verify_password(self,plain_password, hashed_password):
        return self._password_context.verify(plain_password,hashed_password)
    