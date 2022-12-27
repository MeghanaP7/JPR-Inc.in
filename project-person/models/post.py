import sqlalchemy

metadata = sqlalchemy.MetaData()
contact_form = sqlalchemy.Table(
    "contact_form",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("mobile", sqlalchemy.String(length=10), nullable=False),
    sqlalchemy.Column("email", sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column("message", sqlalchemy.String(length=1000), nullable=False),
    #sqlalchemy.Column("ip_address", sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column("browser_type", sqlalchemy.String(length=255), nullable=False),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=False)
)

course_category = sqlalchemy.Table(
    "course_category",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("description", sqlalchemy.String(length=10), nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=False)
)

mentors = sqlalchemy.Table(
    "mentors",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("mentor_id", sqlalchemy.String(length=50), autoincrement=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("middle_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("last_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("education", sqlalchemy.String(length=10), nullable=True),
    sqlalchemy.Column("years_of_experience", sqlalchemy.String(length=50), nullable=True),
    # sqlalchemy.Column("photo", sqlalchemy.String, nullable=True),
    # sqlalchemy.Column("gender", sqlalchemy.Enum, nullable=True),
    sqlalchemy.Column("marital_status", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_addr1", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_addr2", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_addr3", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_city", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_state", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_country", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_mobile", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_landmark", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_addr1", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_addr2", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_addr3", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_city", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_state", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_country", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("alternate_mobile", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_landmark", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=False)
)

courses = sqlalchemy.Table(
    "courses",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("title", sqlalchemy.String(length=50), nullable=False),
    sqlalchemy.Column("course_description", sqlalchemy.String(length=1000), nullable=False),
    sqlalchemy.Column("duration", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("language", sqlalchemy.String(length=50), nullable=False),
    sqlalchemy.Column("course_classroom", sqlalchemy.String(length=255), nullable=False),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=False)
)

mentees = sqlalchemy.Table(
    "mentees",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("mentee_id", sqlalchemy.String(length=50), autoincrement=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("middle_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("last_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("education", sqlalchemy.String(length=10), nullable=True),
    sqlalchemy.Column("years_of_experience", sqlalchemy.String(length=50), nullable=True),
    # sqlalchemy.Column("photo", sqlalchemy.String, nullable=True),
    # sqlalchemy.Column("gender", sqlalchemy.Enum, nullable=True),
    sqlalchemy.Column("marital_status", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_addr1", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_addr2", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_addr3", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_city", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_state", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_country", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_mobile", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_landmark", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_addr1", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_addr2", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_addr3", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_city", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_state", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_country", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("alternate_mobile", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("perm_landmark", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=False)
)

course_contents = sqlalchemy.Table(
    "course_contents",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("duration", sqlalchemy.String(length=1000), nullable=True),
    sqlalchemy.Column("course_id", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=False)
)


course_mentee = sqlalchemy.Table(
    "course_mentee",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("course_id", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("mentee_id", sqlalchemy.String(length=10), nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=False)
)
