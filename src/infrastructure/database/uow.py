from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.renewal_type.interfaces import (
    IRenewalTypeRepo,
    IRenewalTypeUoW,
)
from src.domain.subscription_renewal.interfaces import (
    ISubscriptionRenewalRepo,
    ISubscriptionRenewalUoW,
)
from src.domain.user.interfaces import IUserRepo, IUserUoW


class DatabaseUoW(
    IUserUoW,
    IRenewalTypeUoW,
    ISubscriptionRenewalUoW,
):
    user_repo: IUserRepo
    subscription_renewal_repo: ISubscriptionRenewalRepo
    renewal_type_repo: IRenewalTypeRepo

    def __init__(
        self,
        session: AsyncSession,
        user_repo: Type[IUserRepo],
        subscription_renewal_repo: Type[ISubscriptionRenewalRepo],
        renewal_type_repo: Type[IRenewalTypeRepo],
    ) -> None:
        self.user_repo = user_repo(session)  # type: ignore
        self.subscription_renewal_repo = subscription_renewal_repo(
            session,
        )  # type: ignore
        self.renewal_type_repo = renewal_type_repo(session)  # type: ignore
