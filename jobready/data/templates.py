import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Template(SerializerMixin, SqlAlchemyBase):
    __tablename__ = 'templates'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True,
    )
    preview = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True,
    )
    template_name = sqlalchemy.Column(sqlalchemy.String)
    template_path = sqlalchemy.Column(sqlalchemy.String)
    resumes = orm.relationship(
        'Resume',
        back_populates='template_name',
    )
