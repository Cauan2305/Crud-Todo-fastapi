import bcrypt
class SystemHash:

    def __init__(self) -> None:
        self.salt=bcrypt.gensalt()
    
    def encrypt_password(self,password:str)->bytes:
        hashed=bcrypt.hashpw(password.encode(),self.salt)
        return hashed
    
    def check_password(self,password_hashed:str,password:str)->bool:
        if bcrypt.checkpw(password.encode(),password_hashed.encode()):
            return True
        else :
            return False