from typing import Protocol

from .. import dto


class IUserRepo(Protocol):
    async def user_by_id(self, user_id: int) -> dto.UserDTO:
        ...

    async def add_user(self, create_user: dto.UserCreateDTO) -> dto.UserDTO:
        ...

    async def get_user_referrals_count(self, user_id: int) -> int:
        ...
