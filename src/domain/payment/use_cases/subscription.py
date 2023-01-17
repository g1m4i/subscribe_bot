from .. import dto
from ..interfaces import IPaymentUoW


class PaymentService:
    def __init__(self, uow: IPaymentUoW) -> None:
        self.uow = uow

    async def get_subscription_payment_url(
        self,
        payment_create: dto.CreateSubscriptionPaymentUrl,
    ) -> str:
        return await self.uow.payment_repo.create_subscription_payment_url(
            payment_create,
        )
