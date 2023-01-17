from datetime import datetime
from logging import getLogger

from src.domain.payment import dto
from src.domain.payment.interfaces import IPaymentRepo

from .. import endpoints
from .base import BaseLiqPayAdapter

logger = getLogger(__name__)


class SubscriptionRepo(BaseLiqPayAdapter, IPaymentRepo):
    async def create_subscription_payment_url(
        self,
        payment_create: dto.CreateSubscriptionPaymentUrl,
    ) -> str:
        data = {
            "version": 3,
            "action": "pay",
            "amount": payment_create.amount,
            "currency": payment_create.currency,
            "description": "Оплата підписки",
            "order_id": payment_create.user_id,
            "server_url": payment_create.server_url,
            "subscribe": 1,
            "subscribe_periodicity": payment_create.periodicity,
            "subscribe_date_start": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S",
            ),
        }

        url = await self.create_payment_link(endpoints.CHECKOUT, data)

        return url
