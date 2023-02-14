import sqlalchemy

metadata = sqlalchemy.MetaData()
mentee_info = sqlalchemy.Table(
    "mentee_info",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True,autoincrement=True),
    sqlalchemy.Column("mentee_id",sqlalchemy.String(length=50),nullable=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("last_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("education", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("year_of_experience", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_address", sqlalchemy.String(length=255), nullable=True),
    sqlalchemy.Column("permanent_address", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("gender", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_city", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_state", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_landmark", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_mobile", sqlalchemy.String(length=10), nullable=True),
    sqlalchemy.Column("permanent_city", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("permanent_state", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("permanent_country", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("alternate_mobile", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("email", sqlalchemy.String(length=100), nullable=True),
    sqlalchemy.Column("permanent_landmark", sqlalchemy.String(length=100), nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=True)
)
