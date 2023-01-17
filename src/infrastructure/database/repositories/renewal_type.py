from sqlalchemy import select

from src.domain.renewal_type import dto
from src.domain.renewal_type.interfaces import IRenewalTypeRepo

from ..models import RenewalType
from .base import SQLAlchemyRepo


class RenewalTypeRepo(SQLAlchemyRepo, IRenewalTypeRepo):
    async def type_by_name(self, name: str) -> dto.RenewalTypeDTO:
        statement = select(RenewalType).where(RenewalType.name == name)

        out = await self.session.execute(statement)

        return dto.RenewalTypeDTO.from_orm(out.scalar_one())
