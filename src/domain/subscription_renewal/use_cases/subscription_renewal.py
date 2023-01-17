from src.domain.common.events.dispatcher import EventDispatcher

from .. import dto
from ..events import SubscriptionRenewalCreated
from ..interfaces import ISubscriptionRenewalUoW


class SubscriptionRenewalService:
    def __init__(
        self,
        uow: ISubscriptionRenewalUoW,
        event_dispatcher: EventDispatcher,
    ) -> None:
        self.uow = uow
        self.event_dispatcher = event_dispatcher

    async def add_subscription_renewal(
        self,
        subscription_renewal_create: dto.SubscriptionRenewalCreateDTO,
    ) -> dto.SubscriptionRenewalDTO:
        subscription_renewal = (
            await self.uow.subscription_renewal_repo.add_subscription_renewal(
                subscription_renewal_create,
            )
        )

        await self.event_dispatcher.publish_event(
            SubscriptionRenewalCreated(subscription_renewal),
        )

        return subscription_renewal
