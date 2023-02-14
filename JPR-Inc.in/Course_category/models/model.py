import sqlalchemy

metadata = sqlalchemy.MetaData()
course_category = sqlalchemy.Table(
    "course_category",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("description", sqlalchemy.String(length=10), nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=False)
)
