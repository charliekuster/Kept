from pymongo import MongoClient
from fastapi import Depends

class Database:
    _client = None
    _db = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = MongoClient('mongodb://localhost:27017/')
        return cls._client

    @classmethod
    def get_db(cls, db_name='teste2'):
        if cls._db is None:
            cls._db = cls.get_client()[db_name]
        return cls._db

    @classmethod
    def get_collection(cls, collection_name: str):
        return cls.get_db()[collection_name]

# Dependência para injetar no FastAPI
def get_db():
    db = Database.get_db()
    try:
        yield db
    finally:
        pass  # Como o MongoDB usa conexões persistentes, não precisamos fechar explicitamente
