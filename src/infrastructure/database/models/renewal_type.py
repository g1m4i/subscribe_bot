from sqlalchemy import Column, Enum, Integer, String

from src.domain.renewal_type.models import TypeName

from .base import Base


class RenewalType(Base):
    __tablename__ = "renewal_type"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, Enum(TypeName), nullable=False)
