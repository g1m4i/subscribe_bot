from datetime import datetime
from typing import Optional

from src.domain.common.dto.base import DTO


class UserDTO(DTO):
    id: int
    telegram_id: int
    name: str
    created_time: datetime
    inviter: Optional["UserDTO"]


class UserCreateDTO(DTO):
    telegram_id: int
    name: str
    inviter_id: Optional[int]
