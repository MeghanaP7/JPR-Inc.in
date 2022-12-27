# from pydantic import BaseModel, EmailStr
# from datetime import datetime
#
#
# class ContactForm(BaseModel):
#     id: int
#     name: str
#     mobile: str
#     email: EmailStr
#     message: str
#     created_date: datetime
#     browser_type: str
#
#
# class CourseCategory(BaseModel):
#     id: int
#     name: str
#     description: str
#     created_date: datetime
#     updated_date: datetime
#
#
# class Mentors(BaseModel):
#     id: int
#     mentor_id: str
#     first_name: str
#     middle_name: str
#     last_name: str
#     education: str
#     years_of_experience: str
#     # photo: str
#     # gender: Enum
#     marital_status: bool
#     comm_addr1: str
#     comm_addr2: str
#     comm_addr3: str
#     comm_city: str
#     comm_state: str
#     comm_country: str
#     comm_mobile: int
#     comm_landmark: str
#     perm_addr1: str
#     perm_addr2: str
#     perm_addr3: str
#     perm_city: str
#     perm_state: str
#     perm_country: str
#     alternate_mobile: int
#     perm_landmark: str
#     created_date: datetime
#     updated_date: datetime
#
#
# class Courses(BaseModel):
#     id: int
#     title: str
#     course_description: str
#     duration: str
#     language: str
#     course_classroom: str
#     created_date: datetime
#     updated_date: datetime
#
#
# class CourseContents(BaseModel):
#     id: int
#     name: str
#     duration: str
#     course_id: str
#     created_date: datetime
#     updated_date: datetime
#
#
# class MenteesInfo(BaseModel):
#     id: int
#     mentee_id: str
#     first_name: str
#     middle_name: str
#     last_name: str
#     education: str
#     dob: str
#     years_of_experience: str
#     # photo: str
#     # gender: Enum
#     marital_status: bool
#     email: EmailStr
#     comm_addr1: str
#     comm_addr2: str
#     comm_addr3: str
#     comm_city: str
#     comm_state: str
#     comm_country: str
#     comm_mobile: int
#     comm_landmark: str
#     perm_addr1: str
#     perm_addr2: str
#     perm_addr3: str
#     perm_city: str
#     perm_state: str
#     perm_country: str
#     alternate_mobile: int
#     perm_landmark: str
#     created_date: datetime
#     updated_date: datetime
#
#
# class CourseMentee(BaseModel):
#     id: int
#     course_id: str
#     mentee_id: str
#     created_date: datetime
#     updated_date: datetime
