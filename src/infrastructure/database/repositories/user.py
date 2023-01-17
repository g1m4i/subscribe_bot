from sqlalchemy import insert, select
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import func

from src.domain.user import dto
from src.domain.user.exceptions import UserNotExists
from src.domain.user.interfaces import IUserRepo

from ..models import User
from .base import SQLAlchemyRepo


class UserRepo(SQLAlchemyRepo, IUserRepo):
    async def user_by_id(self, user_id: int) -> dto.UserDTO:
        statement = (
            select(User)
            .where(User.id == user_id)
            .options(joinedload(User.inviter))
        )
        out = await self.session.execute(statement)

        user = out.scalar_one_or_none()

        if not user:
            raise UserNotExists

        return dto.UserDTO.from_orm(user)

    async def add_user(self, create_user: dto.UserCreateDTO) -> dto.UserDTO:
        insert_statement = (
            insert(User).values(**create_user.dict()).returning(User)
        )

        out = await self.session.execute(insert_statement)

        await self.session.commit()
        user = out.scalar_one()

        select_statement = (
            select(User)
            .where(User.id == user.id)
            .options(joinedload(User.inviter))
        )

        out = await self.session.execute(select_statement)

        return dto.UserDTO.from_orm(out.scalar_one())

    async def get_user_referrals_count(self, user_id: int) -> int:
        statement = select(func.coalesce(func.count("*"), 0)).where(
            User.inviter_id == user_id,
        )

        out = await self.session.execute(statement)

        return int(out.scalar_one())
