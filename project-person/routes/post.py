from fastapi import APIRouter
from db import get_database
from fastapi import status, HTTPException
from pydantic import BaseModel, EmailStr
from datetime import datetime
from models.post import contact_form, course_category, mentors, courses, mentee_info
from models.post import course_contents, course_mentee
# from reg import ContactForm, CourseCategory, Mentors, Courses, Mentees
# from reg import CourseContents, CourseMentee
# from schemas import r

router = APIRouter()


class ContactForm(BaseModel):
    id: int
    name: str
    mobile: str
    email: EmailStr
    message: str
    created_date: datetime
    browser_type: str


class CourseCategory(BaseModel):
    id: int
    name: str
    description: str
    created_date: datetime
    updated_date: datetime


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


class Courses(BaseModel):
    id: int
    title: str
    course_description: str
    duration: str
    language: str
    course_classroom: str
    created_date: datetime
    updated_date: datetime


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


class CourseContents(BaseModel):
    id: int
    name: str
    duration: str
    course_id: str
    created_date: datetime
    updated_date: datetime


class CourseMentee(BaseModel):
    id: int
    course_id: str
    mentee_id: str
    created_date: datetime
    updated_date: datetime


@router.post("/contact_form", status_code=status.HTTP_201_CREATED)
async def register(user: ContactForm):
    try:
        db = get_database()
        insert_query = contact_form.insert().values(id=user.id,
                                                    name=user.name,
                                                    mobile=user.mobile,
                                                    email=user.email,
                                                    message=user.message,
                                                    created_date=user.created_date,
                                                    browser_type=user.browser_type
                                                    )

        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@router.get("/contact_form")
async def retrieve_contact_form():
    db = get_database()
    select_query = contact_form.select()
    result = await db.fetch_all(select_query)
    return result


@router.get("/contact_form/{id}")
async def get_contact_form(id: int):
    try:
        db = get_database()
        select_query = contact_form.select().where(contact_form.c.id == id)
        result = await db.fetch_one(select_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])


@router.post("/course_category", status_code=status.HTTP_201_CREATED)
async def post_course(user: CourseCategory):
    try:
        db = get_database()
        insert_query = course_category.insert().values(id=user.id,
                                                       name=user.name,
                                                       description=user.description,
                                                       created_date=user.created_date,
                                                       updated_date=user.updated_date
                                                       )
        await db.execute(insert_query)
        # print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@router.get("/course_category")
async def retrieve_course_category():
    db = get_database()
    select_query = course_category.select()
    result = await db.fetch_all(select_query)
    return result


@router.get("/course_category/{id}")
async def get_course_category(id: int):
    try:
        db = get_database()
        select_query = course_category.select().where(course_category.c.id == id)
        result = await db.fetch_one(select_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])


@router.post("/mentor_info", status_code=status.HTTP_201_CREATED)
async def post_mentor(user: Mentors):
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
async def retrieve_mentor():
    db = get_database()
    select_query = mentors.select()
    result = await db.fetch_all(select_query)
    return result


@router.get("/mentors/{id}")
async def get_mentor(id: int):
    try:
        db = get_database()
        select_query = mentors.select().where(mentors.c.id == id)
        result = await db.fetch_one(select_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])


@router.post("/courses", status_code=status.HTTP_201_CREATED)
async def post_course_data(user: Courses):
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


@router.post("/mentee_info", status_code=status.HTTP_201_CREATED)
async def mentor(user: MenteeInfo):
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


@router.post("/course_contents", status_code=status.HTTP_201_CREATED)
async def register(user: CourseContents):
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


@router.post("/course_mentee", status_code=status.HTTP_201_CREATED)
async def register(user: CourseMentee):
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

