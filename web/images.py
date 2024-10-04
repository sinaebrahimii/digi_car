from fastapi import  APIRouter,Depends,HTTPException,Path,UploadFile
from database import SessionLocal
from starlette import status
from sqlalchemy.orm import Session 
from typing import Annotated
from models.images import Image
from models.products import Product
import boto3
from botocore.exceptions import NoCredentialsError

LIARA_ENDPOINT="https://storage.c2.liara.space"
LIARA_BUCKET_NAME="eager-ardinghelli-jttzxw95u"
LIARA_ACCESS_KEY="p7qhhfp89b5n8grf"
LIARA_SECRET_KEY = "bfcd87fe-0f48-4af1-af3b-3a185782e8bb"  # Make sure to set your secret key


s3 = boto3.client(
    "s3",
    endpoint_url=LIARA_ENDPOINT,
    aws_access_key_id=LIARA_ACCESS_KEY,
    aws_secret_access_key=LIARA_SECRET_KEY
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency= Annotated[Session , Depends(get_db)]

router = APIRouter(prefix="/images",tags=["images"])

@router.post("/{p_id}")
async def create_image(db:db_dependency,photo:UploadFile,p_id:int=Path(gt=0)):
     product = db.query(Product).filter(Product.id == p_id).first()
     if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
     try:
          
        s3.upload_fileobj(photo.file,LIARA_BUCKET_NAME,photo.filename)
        uploaded_file_url=f"https://{LIARA_BUCKET_NAME}.storage.c2.liara.space/{photo.filename}"
        image_model=Image(name=photo.filename,url=uploaded_file_url,product_id=p_id)
        db.add(image_model)
        db.commit()
        return {"message":"image uploaded",
            "filename":photo.filename,
            "url":uploaded_file_url}
     except NoCredentialsError:
            return "Please check your credentials"
     except Exception as e:
           return "error"

   
  
   

    