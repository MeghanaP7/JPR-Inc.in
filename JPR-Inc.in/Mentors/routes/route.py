from fastapi import APIRouter
from db import get_database
from fastapi import status, HTTPException
from pydantic import BaseModel
from datetime import datetime
from models.model import mentors

router = APIRouter()

class Mentors(BaseModel):
    id: int
    mentor_id: str
    first_name: str
    middle_name: str
    last_name: str
    education: str
    years_of_experience: str
    # photo: str
    # gender: Enum
    marital_status: bool
    comm_addr1: str
    comm_addr2: str
    comm_addr3: str
    comm_city: str
    comm_state: str
    comm_country: str
    comm_mobile: int
    comm_landmark: str
    perm_addr1: str
    perm_addr2: str
    perm_addr3: str
    perm_city: str
    perm_state: str
    perm_country: str
    alternate_mobile: int
    perm_landmark: str
    created_date: datetime
    updated_date: datetime

class MentorsPartialUpdate(BaseModel):
    id: int
    comm_addr1: str
    comm_addr2: str
    comm_addr3: str
    comm_city: str
    comm_state: str
    comm_country: str
    comm_mobile: int
    comm_landmark: str
    perm_addr1: str
    perm_addr2: str
    perm_addr3: str
    perm_city: str
    perm_state: str
    perm_country: str
    alternate_mobile: int
    perm_landmark: str

@router.post("/mentor_info", status_code=status.HTTP_201_CREATED)
async def data(user: Mentors):
    try:
        db = get_database()
        insert_query = mentors.insert().values(id=user.id,
                                               mentor_id=user.mentor_id,
                                               first_name=user.first_name,
                                               middle_name=user.middle_name,
                                               last_name=user.last_name,
                                               education=user.education,
                                               years_of_experience=user.years_of_experience,
                                               # photo=user.photo,
                                               # gender=Gender.,
                                               marital_status=user.marital_status,
                                               comm_addr1=user.comm_addr1,
                                               comm_addr2=user.comm_addr2,
                                               comm_addr3=user.comm_addr3,
                                               comm_city=user.comm_city,
                                               comm_state=user.comm_state,
                                               comm_country=user.comm_country,
                                               comm_mobile=user.comm_mobile,
                                               comm_landmark=user.comm_landmark,
                                               perm_addr1=user.perm_addr1,
                                               perm_addr2=user.perm_addr2,
                                               perm_addr3=user.perm_addr3,
                                               perm_city=user.perm_city,
                                               perm_state=user.perm_state,
                                               perm_country=user.perm_country,
                                               alternate_mobile=user.alternate_mobile,
                                               perm_landmark=user.perm_landmark,
                                               created_date=user.created_date,
                                               updated_date=user.updated_date)
        await db.execute(insert_query)
        # print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@router.get("/mentors")
async def retrieve_mentor_data():
    db = get_database()
    select_query = mentors.select()
    result = await db.fetch_all(select_query)
    return result


@router.get("/mentors/{id}")
async def get_mentor_data(id: int):
    try:
        db = get_database()
        select_query = mentors.select().where(mentors.c.id == id)
        result = await db.fetch_one(select_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])

@router.delete("/mentors/{id}", status_code=status.HTTP_200_OK)
async def delete_mentor_data(id: int):
    try:
        db = get_database()
        delete_query = (mentors.delete().where(mentors.c.id == id))
        result = await db.fetch_all(delete_query)
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='successfully deleted')

@router.put("/mentors/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_mentor_data(id: int, user: Mentors):
    try:
        db=get_database()
        update_query = (mentors.update().where(mentors.c.id == id).values(id=user.id,
                                                                          mentor_id=user.mentor_id,
                                                                          first_name=user.first_name,
                                                                          middle_name=user.middle_name,
                                                                          last_name=user.last_name,
                                                                          education=user.education,
                                                                          years_of_experience=user.years_of_experience,
                                                                          # photo=user.photo,
                                                                          # gender=Gender.,
                                                                          marital_status=user.marital_status,
                                                                          comm_addr1=user.comm_addr1,
                                                                          comm_addr2=user.comm_addr2,
                                                                          comm_addr3=user.comm_addr3,
                                                                          comm_city=user.comm_city,
                                                                          comm_state=user.comm_state,
                                                                          comm_country=user.comm_country,
                                                                          comm_mobile=user.comm_mobile,
                                                                          comm_landmark=user.comm_landmark,
                                                                          perm_addr1=user.perm_addr1,
                                                                          perm_addr2=user.perm_addr2,
                                                                          perm_addr3=user.perm_addr3,
                                                                          perm_city=user.perm_city,
                                                                          perm_state=user.perm_state,
                                                                          perm_country=user.perm_country,
                                                                          alternate_mobile=user.alternate_mobile,
                                                                          perm_landmark=user.perm_landmark,
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

@router.patch("/mentors/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_mentor_data(id: int, user: MentorsPartialUpdate):
    try:
        db = get_database()
        update_query =(mentors.update().where(mentors.c.id == id).values(id=user.id,
                                                                         comm_addr1=user.comm_addr1,
                                                                         comm_addr2=user.comm_addr2,
                                                                         comm_addr3=user.comm_addr3,
                                                                         comm_city=user.comm_city,
                                                                         comm_state=user.comm_state,
                                                                         comm_country=user.comm_country,
                                                                         comm_mobile=user.comm_mobile,
                                                                         comm_landmark=user.comm_landmark,
                                                                         perm_addr1=user.perm_addr1,
                                                                         perm_addr2=user.perm_addr2,
                                                                         perm_addr3=user.perm_addr3,
                                                                         perm_city=user.perm_city,
                                                                         perm_state=user.perm_state,
                                                                         perm_country=user.perm_country,
                                                                         alternate_mobile=user.alternate_mobile,
                                                                         perm_landmark=user.perm_landmark,
                                                                         ))                                                             
        result = await db.fetch_one(update_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details') 
