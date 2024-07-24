from fastapi import FastAPI
import models
from database import  engine,Base
from web import products

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(products.router)
