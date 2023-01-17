from datetime import datetime
from typing import Optional

from src.domain.common.dto.base import DTO
from src.domain.renewal_type.dto import RenewalTypeDTO

from .user import UserDTO


class SubscriptionRenewalDTO(DTO):
    id: int
    days: int
    user: UserDTO
    renewal_type: RenewalTypeDTO
    payment_id: Optional[int]
    created_time: datetime


class SubscriptionRenewalCreateDTO(DTO):
    days: int
    user_id: int
    payment_id: Optional[int]
    renewal_type_id: int
