from fastapi import APIRouter
from db import get_database
from fastapi import status, HTTPException
from pydantic import BaseModel
from datetime import datetime
from models.model import course_mentee


router = APIRouter()


class CourseMentee(BaseModel):
    id: int
    course_id: str
    mentee_id: str
    created_date: datetime
    updated_date: datetime

class CourseMenteePartialUpdate(BaseModel):
    id: int
    course_id: str
    mentee_id: str



@router.post("/course_mentee", status_code=status.HTTP_201_CREATED)
async def data(user: CourseMentee):
    try:
        db = get_database()
        insert_query = course_mentee.insert().values(id=user.id,
                                                     course_id=user.course_id,
                                                     mentee_id=user.mentee_id,
                                                     created_date=user.created_date,
                                                     updated_date=user.updated_date
                                                     )
        await db.execute(insert_query)
        # print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@router.get("/course_mentee")
async def retrieve_course_mentee():
    db = get_database()
    select_query = course_mentee.select()
    result = await db.fetch_all(select_query)
    return result


@router.get("/course_mentee/{id}")
async def get_course_mentee(id: int):
    try:
        db = get_database()
        select_query = course_mentee.select().where(course_mentee.c.id == id)
        result = await db.fetch_one(select_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])

@router.delete("/course_mentee/{id}", status_code=status.HTTP_200_OK)
async def delete_course_mentee(id: int):
    try:
        db = get_database()
        delete_query = (course_mentee.delete().where(course_mentee.c.id == id))
        result = await db.fetch_all(delete_query)
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='successfully deleted')

@router.put("/course_mentee/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_course_mentee(id: int, user: CourseMentee):
    try:
        db=get_database()
        update_query = (course_mentee.update().where(course_mentee.c.id == id).values(id=user.id,
                                                                                      course_id=user.course_id,
                                                                                      mentee_id=user.mentee_id,
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

@router.patch("/course_mentee/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_course_mentee(id: int, user: CourseMenteePartialUpdate):
    try:
        db = get_database()
        update_query =(course_mentee.update().where(course_mentee.c.id == id).values(
                                                                                    id= user.id,
                                                                                    course_id=user.course_id,
                                                                                    mentee_id=user.mentee_id,
                                                                                    ))                                                                 
        result = await db.fetch_one(update_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')    

