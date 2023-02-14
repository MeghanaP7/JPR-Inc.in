import sqlalchemy

metadata = sqlalchemy.MetaData()
course_mentee = sqlalchemy.Table(
    "course_mentee",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("course_id", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("mentee_id", sqlalchemy.String(length=10), nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=False)
)
