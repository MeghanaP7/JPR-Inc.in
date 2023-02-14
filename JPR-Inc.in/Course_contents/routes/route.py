from fastapi import APIRouter
from db import get_database
from fastapi import status, HTTPException
from pydantic import BaseModel
from datetime import datetime
from models.model import course_contents

router = APIRouter()

class CourseContents(BaseModel):
    id: int
    name: str
    duration: str
    course_id: str
    created_date: datetime
    updated_date: datetime

class CourseContentsPartialUpdate(BaseModel):
    id: int
    duration: str
    course_id: str


@router.post("/course_contents", status_code=status.HTTP_201_CREATED)
async def data(user: CourseContents):
    try:
        db = get_database()
        insert_query = course_contents.insert().values(id=user.id,
                                                       name=user.name,
                                                       duration=user.duration,
                                                       course_id=user.course_id,
                                                       created_date=user.created_date,
                                                       updated_date=user.updated_date)
        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@router.get("/course_contents")
async def retrieve_course_contents():
    db = get_database()
    select_query = course_contents.select()
    result = await db.fetch_all(select_query)
    return result


@router.get("/course_contents/{id}")
async def get_course_contents(id: int):
    try:
        db = get_database()
        select_query = course_contents.select().where(course_contents.c.id == id)
        result = await db.fetch_one(select_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])

@router.delete("/course_contents/{id}", status_code=status.HTTP_200_OK)
async def delete_course_contents(id: int):
    try:
        db = get_database()
        delete_query = (course_contents.delete().where(course_contents.c.id == id))
        result = await db.fetch_all(delete_query)
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='successfully deleted')

@router.put("/course_contents/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_course_contents(id: int, user: CourseContents):
    try:
        db=get_database()
        update_query = (course_contents.update().where(course_contents.c.id == id).values(id=user.id,
                                                                                          name=user.name,
                                                                                          duration=user.duration,
                                                                                          course_id=user.course_id,
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

@router.patch("/course_contents/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_course_contents(id: int, user: CourseContentsPartialUpdate):
    try:
        db = get_database()
        update_query =(course_contents.update().where(course_contents.c.id == id).values(
                                                                                    id= user.id,
                                                                                    duration=user.duration,
                                                                                    course_id=user.course_id,
                                                                                    ))                                                                 
        result = await db.fetch_one(update_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')    

