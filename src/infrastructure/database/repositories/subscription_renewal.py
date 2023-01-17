from sqlalchemy import insert, select
from sqlalchemy.orm import joinedload

from src.domain.subscription_renewal import dto
from src.domain.subscription_renewal.interfaces import ISubscriptionRenewalRepo

from ..models import SubscriptionRenewal
from .base import SQLAlchemyRepo


class SubscriptionRenewalRepo(SQLAlchemyRepo, ISubscriptionRenewalRepo):
    async def add_subscription_renewal(
        self,
        subscription_renewal_create: dto.SubscriptionRenewalCreateDTO,
    ) -> dto.SubscriptionRenewalDTO:
        insert_statement = (
            insert(SubscriptionRenewal)
            .values(**subscription_renewal_create.dict())
            .returning(SubscriptionRenewal)
        )

        out = await self.session.execute(insert_statement)
        await self.session.commit()

        select_statement = (
            select(SubscriptionRenewal)
            .where(SubscriptionRenewal.id == out.scalar_one().id)
            .options(
                joinedload(SubscriptionRenewal.user).subqueryload(
                    SubscriptionRenewal.renewal_type,
                ),
            )
        )

        out = await self.session.execute(select_statement)

        return dto.SubscriptionRenewalDTO.from_orm(out.scalar_one())
