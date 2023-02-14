from fastapi import APIRouter
from db import get_database
from fastapi import status, HTTPException
from pydantic import BaseModel, EmailStr
from datetime import datetime
from models.model import mentee_info



router = APIRouter()

class MenteeInfo(BaseModel):
    id: int
    mentee_id: str
    first_name: str
    last_name: str
    education: str
    year_of_experience: str
    comm_address: str
    permanent_address: str
    gender: str
    comm_city: str
    comm_state: str
    comm_landmark: str
    comm_mobile: str
    permanent_city: str
    permanent_state: str
    permanent_country: str
    alternate_mobile: str
    email: EmailStr
    permanent_landmark: str
    created_date: datetime
    updated_date: datetime

class MenteeInfoPartialUpdate(BaseModel):
    id: int
    comm_address: str
    permanent_address: str
    gender: str
    comm_city: str
    comm_state: str
    comm_landmark: str
    comm_mobile: str
    permanent_city: str
    permanent_state: str
    permanent_country: str
    alternate_mobile: str
    email: EmailStr
    permanent_landmark: str

@router.post("/mentee_info", status_code=status.HTTP_201_CREATED)
async def data(user: MenteeInfo):
    try:
        db = get_database()
        insert_query = mentee_info.insert().values(
                                                   id=user.id,
                                                   mentee_id=user.mentee_id,
                                                   first_name=user.first_name,
                                                   last_name=user.last_name,
                                                   education=user.education,
                                                   year_of_experience=user.year_of_experience,
                                                   comm_address=user.comm_address,
                                                   permanent_address=user.permanent_address,
                                                   gender=user.gender,
                                                   comm_city=user.comm_city,
                                                   comm_state=user.comm_state,
                                                   comm_mobile=user.comm_mobile,
                                                   comm_landmark=user.comm_landmark,
                                                   permanent_city=user.permanent_city,
                                                   permanent_state=user.permanent_state,
                                                   permanent_country=user.permanent_country,
                                                   alternate_mobile=user.alternate_mobile,
                                                   email=user.email,
                                                   permanent_landmark=user.permanent_landmark,
                                                   created_date=user.created_date,
                                                   updated_date=user.updated_date
                                                   )
        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@router.get("/mentees_data")
async def retrieve_mentees_data():
    db = get_database()
    select_query = mentee_info.select()
    result = await db.fetch_all(select_query)
    return result


@router.get("/mentees_data/{id}")
async def get_mentees_data(id: int):
    try:
        db = get_database()
        select_query = mentee_info.select().where(mentee_info.c.id == id)
        result = await db.fetch_one(select_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])

@router.delete("/MenteeInfo/{id}", status_code=status.HTTP_200_OK)
async def delete_mentee_data(id: int):
    try:
        db = get_database()
        delete_query = (mentee_info.delete().where(mentee_info.c.id == id))
        result = await db.fetch_all(delete_query)
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='successfully deleted')

@router.put("/MenteeInfo/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_mentee_data(id: int, user: MenteeInfo):
    try:
        db=get_database()
        update_query = (mentee_info.update().where(mentee_info.c.id == id).values(id=user.id,
                                                                          mentee_id=user.mentee_id,
                                                                          first_name=user.first_name,
                                                                          last_name=user.last_name,
                                                                          education=user.education,
                                                                          year_of_experience=user.year_of_experience,
                                                                          comm_address=user.comm_address,
                                                                          permanent_address=user.permanent_address,
                                                                          gender=user.gender,
                                                                          comm_city=user.comm_city,
                                                                          comm_state=user.comm_state,
                                                                          comm_mobile=user.comm_mobile,
                                                                          comm_landmark=user.comm_landmark,
                                                                          permanent_city=user.permanent_city,
                                                                          permanent_state=user.permanent_state,
                                                                          permanent_country=user.permanent_country,
                                                                          alternate_mobile=user.alternate_mobile,
                                                                          email=user.email,
                                                                          permanent_landmark=user.permanent_landmark,
                                                                          created_date=user.created_date,
                                                                          updated_date=user.updated_date
                                                                          ))                    
        result = await db.fetch_one(update_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')

@router.patch("/MenteeInfo/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_mentee_data(id: int, user: MenteeInfoPartialUpdate):
    try:
        db = get_database()
        update_query =(mentee_info.update().where(mentee_info.c.id == id).values(id=user.id,
                                                                          mentee_id=user.mentee_id,
                                                                          comm_address=user.comm_address,
                                                                          permanent_address=user.permanent_address,
                                                                          gender=user.gender,
                                                                          comm_city=user.comm_city,
                                                                          comm_state=user.comm_state,
                                                                          comm_mobile=user.comm_mobile,
                                                                          comm_landmark=user.comm_landmark,
                                                                          permanent_city=user.permanent_city,
                                                                          permanent_state=user.permanent_state,
                                                                          permanent_country=user.permanent_country,
                                                                          alternate_mobile=user.alternate_mobile,
                                                                          email=user.email,
                                                                          permanent_landmark=user.permanent_landmark,
                                                                          ))                                                             
        result = await db.fetch_one(update_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details') 
