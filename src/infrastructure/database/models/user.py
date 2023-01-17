from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger, nullable=False)
    name = Column(String, nullable=False)
    created_time = Column(DateTime, server_default=func.now())
    inviter_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    inviter = relationship("User")
