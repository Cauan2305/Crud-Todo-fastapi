from app.core.users.entity import Users
from datetime import datetime,timedelta
import jwt,uuid

class Token:
    def __init__(self) -> None:
        pass

    def generate_payload(self,user:dict):
        return {
            "user_id":user['id'],
            "session_id":str(uuid.uuid4()),
            "expires":(datetime.now()+timedelta(1)).isoformat()
        }
    def generate_token_session(self,user:Users):
        encoded_jwt = jwt.encode(self.generate_payload(user), "secret", algorithm="HS256")
        return encoded_jwt
    
    def decode_token(self,token):
        return jwt.decode(token, "secret", algorithms=["HS256"])