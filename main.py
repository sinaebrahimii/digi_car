from fastapi import FastAPI
from database import  engine,Base
from web import products,categories,users,auth,reviews,images

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(products.router)
app.include_router(categories.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(reviews.router)
app.include_router(images.router)