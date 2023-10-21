from abc import ABC,abstractmethod

class DatabaseInterface(ABC):

    @abstractmethod
    def insert(self,table_name:str,data_to_insert:dict):
        pass

    @abstractmethod
    def update(self,table_name:str,query:dict,data_to_update:dict,upsert:bool=False):
        pass

    @abstractmethod
    def find(self,table_name:str,query:dict,sort:list[tuple]=None):
        pass