import uuid
from sqlalchemy import Column, Integer, String
from core import Settings


class CourseModel(Settings.DB_BASE_MODEL):
    __tablename__ = 'courses'
    id = Column(String(40),
                primary_key=True,
                default=str(uuid.uuid4()),
                unique=True,
                nullable=False)
    title: str = Column(String(100))
    lessons: int = Column(Integer)
    hours: int = Column(Integer)
