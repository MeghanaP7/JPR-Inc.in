import sqlalchemy

metadata = sqlalchemy.MetaData()
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
