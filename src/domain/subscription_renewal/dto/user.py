from datetime import datetime

from src.domain.common.dto.base import DTO


class UserDTO(DTO):
    id: int
    telegram_id: int
    name: str
    created_time: datetime
