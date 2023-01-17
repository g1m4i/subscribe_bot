from typing import Protocol

from .. import dto


class IPaymentRepo(Protocol):
    async def create_subscription_payment_url(
        self,
        payment_create: dto.CreateSubscriptionPaymentUrl,
    ) -> str:
        ...
