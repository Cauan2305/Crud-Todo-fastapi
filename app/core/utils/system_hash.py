import bcrypt
class SystemHash:

    def __init__(self) -> None:
        self.salt=bcrypt.gensalt()
    
    def encrypt_password(self,password:str)->bytes:
        hashed=bcrypt.hashpw(password.encode(),self.salt)
        return hashed
    
    def check_password(self,password:str)->bool:
        if bcrypt.checkpw(password.encode(),self.encrypt_password(password)):
            return True
        else :
            return False