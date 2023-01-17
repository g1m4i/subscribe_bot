from typing import Protocol

from .. import dto


class ISubscriptionRenewalRepo(Protocol):
    async def add_subscription_renewal(
        self,
        subscription_renewal_create: dto.SubscriptionRenewalCreateDTO,
    ) -> dto.SubscriptionRenewalDTO:
        ...
