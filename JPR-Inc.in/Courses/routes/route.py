from fastapi import APIRouter
from db import get_database
from fastapi import status, HTTPException
from pydantic import BaseModel
from datetime import datetime
from models.model import courses


router = APIRouter()

class Courses(BaseModel):
    id: int
    title: str
    course_description: str
    duration: str
    language: str
    course_classroom: str
    created_date: datetime
    updated_date: datetime

class CoursesPartialUpdate(BaseModel):
    id: int
    title: str
    course_description: str
    duration: str
    language: str
    course_classroom: str

@router.post("/courses", status_code=status.HTTP_201_CREATED)
async def data(user: Courses):
    try:
        db = get_database()
        insert_query = courses.insert().values(id=user.id,
                                               title=user.title,
                                               course_description=user.course_description,
                                               duration=user.duration,
                                               language=user.language,
                                               course_classroom=user.course_classroom,
                                               created_date=user.created_date,
                                               updated_date=user.updated_date)
        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@router.get("/courses")
async def retrieve_courses():
    db = get_database()
    select_query = courses.select()
    result = await db.fetch_all(select_query)
    return result


@router.get("/courses/{id}")
async def get_courses(id: int):
    try:
        db = get_database()
        select_query = courses.select().where(courses.c.id == id)
        result = await db.fetch_one(select_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        # return result

@router.delete("/courses/{id}", status_code=status.HTTP_200_OK)
async def delete_courses(id: int):
    try:
        db = get_database()
        delete_query = (courses.delete().where(courses.c.id == id))
        result = await db.fetch_all(delete_query)
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='successfully deleted')

@router.put("/courses/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_courses(id: int, user: Courses):
    try:
        db=get_database()
        update_query = (courses.update().where(courses.c.id == id).values(id=user.id,
                                                                                      title=user.title,
                                                                                      course_description=user.course_description,
                                                                                      duration=user.duration,
                                                                                      language=user.language,
                                                                                      course_classroom=user.course_classroom,
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

@router.patch("/courses/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_courses(id: int, user: CoursesPartialUpdate):
    try:
        db = get_database()
        update_query =(courses.update().where(courses.c.id == id).values(id=user.id,
                                                                                     title=user.title,
                                                                                     course_description=user.course_description,
                                                                                     duration=user.duration,
                                                                                     language=user.language,
                                                                                     course_classroom=user.course_classroom,
                                                                                     ))                                                                 
        result = await db.fetch_one(update_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')    


