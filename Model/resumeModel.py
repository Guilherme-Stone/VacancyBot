from sqlalchemy import Integer, Column, String
from Config.settings import Base

class ResumeModel(Base):
    __tablename__ = "resumeModel"
    id = Column(Integer, primary_key=True)
    resume = Column(String,nullable=False)
    url = Column(String,nullable=False)