from fastapi import FastAPI
import models
from database import  engine
from web import products

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(products.router)
