from fastapi import FastAPI, Depends, Response, status, HTTPException
import models
from database import engine, get_db
from pydantic import BaseModel
from sqlalchemy.orm import Session
import uuid
from typing import Optional

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class Scheme_Business(BaseModel):
    name: str
    domain: str
    business_type: str
    description: str

class Member(BaseModel):
    business_id: str
    member_id: str



@app.get("/")
def root():
    return {"msg":"Hello"}

@app.get("/all_business")
def get_data(db: Session = Depends(get_db)):
    data = db.query(models.Business).all()
    return data

@app.get("/business/{id}")
def get_profile(id: uuid.UUID, db: Session = Depends(get_db)):
    data = db.query(models.Business).filter(models.Business.business_id == id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product with id: {id} is not defind")
    return data

@app.post("/create_business")
def create_profile(create: Scheme_Business, db: Session = Depends(get_db)):
    existing_profile = db.query(models.Business).filter(models.Business.domain == create.domain).first()
    if existing_profile:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product with this domain already exists")
    # new_profile = models.Profile(**create.dict())
    new_profile = models.Business(
        name=create.name,
        domain=create.domain,
        business_type=create.business_type,
        description=create.description
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

@app.delete("/delete_business{id}")
def delete_profile(id: uuid.UUID, db: Session = Depends(get_db), status_code=status.HTTP_204_NO_CONTENT):
    deleted = db.query(models.Business).filter(models.Business.business_id == id)
    if deleted.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} dose not exist")
    deleted.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@app.put("/update_business/{id}")
def update_post(id: uuid.UUID, updated_profile: Scheme_Business, db: Session = Depends(get_db)):
    profile_query = db.query(models.Business).filter(models.Business.business_id == id)  # เปลี่ยนจาก models.Post เป็น models.Profile
    profile = profile_query.first()
    if profile is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"profile with id: {id} does not exist")
    print(profile.domain)
    print(updated_profile.domain)
    check = db.query(models.Business).filter(models.Business.domain == updated_profile.domain).first()
    if check:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sammm")
    profile_query.update(updated_profile.dict(exclude_unset=True), synchronize_session=False)  # ใช้ exclude_unset เพื่ออัปเดตเฉพาะฟิลด์ที่ได้รับค่าใหม่
    db.commit()
    return profile_query.first()

