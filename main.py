from fastapi import FastAPI
import models
from database import  engine,Base
from web import products,categories,users,auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(products.router)
app.include_router(categories.router)
app.include_router(users.router)
app.include_router(auth.router)