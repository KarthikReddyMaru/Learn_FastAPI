from fastapi import FastAPI
from database.database import session, engine
from models.Product import Base

def init():
    Base.metadata.create_all(bind = engine)

init()

app = FastAPI()

@app.get("/")
def main():
    return "Hello from learn-fastapi!"