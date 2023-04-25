import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Resume(SerializerMixin, SqlAlchemyBase):
    __tablename__ = 'resumes'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True,
    )
    user_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')
    )
    template_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('templates.id')
    )
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.LargeBinary, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    place_of_residence = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    skills = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    expierence = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    education = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    achievments = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    template_name = orm.relationship('Template')
    user = orm.relationship('User')
