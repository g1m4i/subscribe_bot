from .. import dto
from ..interfaces import IUserUoW


class UserService:
    def __init__(self, uow: IUserUoW) -> None:
        self.uow = uow

    async def create_user(self, create_user: dto.UserCreateDTO) -> dto.UserDTO:
        return await self.uow.user_repo.add_user(create_user)

    async def get_user(self, user_id: int) -> dto.UserDTO:
        return await self.uow.user_repo.user_by_id(user_id)

    async def get_user_referrals_count(self, user_id: int) -> int:
        return await self.uow.user_repo.get_user_referrals_count(user_id)
