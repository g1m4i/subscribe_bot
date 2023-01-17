from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .base import Base
from .renewal_type import RenewalType
from .user import User


class SubscriptionRenewal(Base):
    __tablename__ = "subscription_renewal"

    id = Column(Integer, autoincrement=True, primary_key=True)
    created_time = Column(DateTime, server_default=func.now())
    days = Column(Integer, nullable=False)
    renewal_type_id = Column(
        Integer,
        ForeignKey("renewal_type.id"),
        nullable=False,
    )
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    payment_id = Column(Integer, nullable=True)

    user = relationship(User)
    renewal_type = relationship(RenewalType)
