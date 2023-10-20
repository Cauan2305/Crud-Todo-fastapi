import os
credentials={
    "MONGO_CONNECTION_URI":os.getenv('MONGO_CONNECTION_URI'),
    "DATABASE_NAME":os.getenv('DATABASE_NAME',"AppTodo"),
    "BASE_URL":os.getenv('BASE_URL','http://127.0.0.1:8000/'),
    "COOKIE_DOMAIN":os.getenv('COOKIE_DOMAIN','http://127.0.0.1')
}