from typing import Dict, List, Optional
from app.core.db.interface import DatabaseInterface
from pymongo import MongoClient
from config import credentials

from typing import Dict,List,Optional

class Database(DatabaseInterface):

    def __init__(self,database_name:str) -> None:
        self._db_client=MongoClient(credentials['MONGO_CONNECTION_URI'])[database_name]
    
    def insert(self, table_name: str, data_to_insert: dict) -> Optional[str]:
        result=self._db_client[table_name].insert_one(data_to_insert)
        if not result.acknowledged:
            raise DbErrorOperations("It was not possible to perform the data insertion operation")
        return result.inserted_id
    

    def update(self, table_name: str, query: dict, data: dict,upsert:bool=False) -> bool:
        result=self._db_client[table_name].update_one(query,{'$set':data},upsert)
        if result.matched_count <1:
            raise DbErrorOperations("Id Not Found")
        return True
    
    def find(self, table_name: str, query: dict) -> List[Dict] | None:
        return list(self._db_client[table_name].find(query))

class DbErrorOperations(Exception):
    def __init__(self, message:str) -> None:
        super().__init__(message)