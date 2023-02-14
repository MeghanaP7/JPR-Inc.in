import sqlalchemy

metadata = sqlalchemy.MetaData()
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
